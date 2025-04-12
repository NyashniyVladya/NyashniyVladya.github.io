# -*- coding: utf-8 -*-
"""
@author: Vladya
"""


import pathlib
import requests
import json


BASEDIR = pathlib.Path(__file__).parent.resolve(True)
VERSIONS = BASEDIR.joinpath("versions")
JSON = BASEDIR.joinpath("versionsSummary.json")

MAIN_URL = "https://nyashniyvladya.github.io/torBundles/versions"


def main():

    result = {}

    for version_dir in VERSIONS.iterdir():
        _version = tuple(map(int, version_dir.name.split('.')))
        _key = '.'.join(map(str, _version))
        _dir_url = requests.compat.urljoin(MAIN_URL, version_dir.name)
        for bundle in version_dir.iterdir():
            _url = requests.compat.urljoin(_dir_url, bundle.name)
            result.setdefault(_key, {})[bundle.name] = _url

    with JSON.open('w', encoding="utf_8") as _file:
        json.dump(result, _file, ensure_ascii=False, indent=4)
