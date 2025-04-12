# -*- coding: utf-8 -*-
"""
@author: Vladya
"""


import pathlib
import json


BASEDIR = pathlib.Path(__file__).parent.resolve(True)
VERSIONS = BASEDIR.joinpath("versions")
JSON = BASEDIR.joinpath("versionsSummary.json")

URL = "https://nyashniyvladya.github.io/torBundles/versions/{0}/{1}"


def main():

    result = {}

    for version_dir in VERSIONS.iterdir():
        _version = tuple(map(int, version_dir.name.split('.')))
        _key = '.'.join(map(str, _version))
        for bundle in version_dir.iterdir():
            _url = URL.format(version_dir.name, bundle.name)
            result.setdefault(_key, {})[bundle.name] = _url

    with JSON.open('w', encoding="utf_8") as _file:
        json.dump(result, _file, ensure_ascii=False, indent=4)
