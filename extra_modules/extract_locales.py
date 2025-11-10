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


def create_locale_json():

    tags = extract_locales(*map(lambda p: site_dir.joinpath(p), TARGET_FILES))

    output_fn = locales_dir.joinpath(SOURCE_LANGUAGE).with_suffix(".json")
    output_fn.parent.mkdir(parents=True, exist_ok=True)

    with output_fn.open('w', encoding="utf_8") as _file:
        json.dump(tags, _file, ensure_ascii=False, indent=4, sort_keys=True)
