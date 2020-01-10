# Native imports
from typing import List
from pathlib import Path
from json import load

__LOCAL = Path(__file__).parents[1].joinpath('data')


def readData(filename: str) -> List[dict]:
    with open(__LOCAL.joinpath(filename)) as dataJson:
        serializedObject = load(dataJson)

    return serializedObject
