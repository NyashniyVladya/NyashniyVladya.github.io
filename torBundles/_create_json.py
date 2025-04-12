# -*- coding: utf-8 -*-
"""
@author: Vladya
"""


import pathlib
import json
import requests


BASEDIR = pathlib.Path(__file__).parent.resolve(True)
VERSIONS = BASEDIR.joinpath("versions")
JSON = BASEDIR.joinpath("versionsSummary.json")

URL = "https://nyashniyvladya.github.io/{0}/{1}/{{0}}/{{1}}".format(
    requests.compat.quote(BASEDIR.name),
    requests.compat.quote(VERSIONS.name)
)


def main():

    result = {}

    for version_dir in VERSIONS.iterdir():
        _version = tuple(map(int, version_dir.name.split('.')))
        _key = '.'.join(map(str, _version))
        for bundle in version_dir.iterdir():
            _url = URL.format(
                requests.compat.quote(version_dir.name),
                requests.compat.quote(bundle.name)
            )
            result.setdefault(_key, {})[bundle.name] = _url

    with JSON.open('w', encoding="utf_8") as _file:
        json.dump(result, _file, ensure_ascii=False, indent=4)
