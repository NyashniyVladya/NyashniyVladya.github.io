# -*- coding: utf-8 -*-
"""
@author: Vladya
"""

import pathlib
import json
from bs4 import BeautifulSoup

SOURCE_LANGUAGE = "ru"
TAG_NAME = "data-i18n"

TARGET_FILES = ("index.html", "docs.html", "gui.html")


site_dir = pathlib.Path(__file__).absolute().parent.parent
locales_dir = site_dir.joinpath("locales")


def extract_locales(*fns):
    tags = {}
    for fn in fns:
        fn = pathlib.Path(fn).absolute()
        if not fn.is_file():
            raise ValueError(f"No {fn} was found")
        with fn.open('r', encoding="utf_8") as _file:
            soup = BeautifulSoup(_file.read(), "lxml")
        for tag in soup.find_all(lambda tag: tag.has_attr(TAG_NAME)):
            key = tag.get(TAG_NAME)
            value = "".join(map(str, tag.contents))
            if key in tags:
                if tags[key] != value:
                    raise RuntimeError(
                        (
                            f"Different values for one key \"{key}\": "
                            f"\"{tags[key]}\" and \"{value}\""
                        )
                    )
                continue
            tags[key] = value
    return tags


def _translate_dict(dct, src_lng, target_lng, locale_tr):

    strings = list(dct.values())

    while True:

        if not strings:
            break

        part = []
        for s in strings:
            _len = locale_tr.get_string_len(
                '\n'.join(part),
                target_lng,
                src_lng
            )
            if _len >= locale_tr.SYMB_LIMIT:
                if part:
                    part.pop(-1)
                break
            part.append(s)

        assert part
        locale_tr.translate(
            '\n'.join(part),
            target_lng,
            src_lng,
            None,
            False
        )
        for p in part:
            if p in strings:
                strings.remove(p)

    return dict(
        map(
            lambda a: (
                a[0],
                locale_tr.translate(a[1], target_lng, src_lng, None, False)
            ),
            dct.items()
        )
    )


def create_locale_json(locale_tr, *need_langs):

    source_lng = locale_tr.get_lang_name(SOURCE_LANGUAGE, True)
    need_langs = set(
        map(
            lambda a: locale_tr.get_lang_name(a, True),
            need_langs
        )
    )
    need_langs.discard(source_lng)

    tags = extract_locales(*map(lambda p: site_dir.joinpath(p), TARGET_FILES))

    output_fn = locales_dir.joinpath(source_lng).with_suffix(".json")
    output_fn.parent.mkdir(parents=True, exist_ok=True)

    with output_fn.open('w', encoding="utf_8") as _file:
        json.dump(tags, _file, ensure_ascii=False, indent=4, sort_keys=True)

    for need_lang in need_langs:

        tr_tags = _translate_dict(tags, source_lng, need_lang, locale_tr)

        output_fn = locales_dir.joinpath(need_lang).with_suffix(".json")
        output_fn.parent.mkdir(parents=True, exist_ok=True)

        with output_fn.open('w', encoding="utf_8") as _file:
            json.dump(tr_tags, _file, ensure_ascii=False, indent=4, sort_keys=True)
