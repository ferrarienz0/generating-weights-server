from typing import List
from pathlib import Path
import json

__LOCAL = Path(__file__).parents[1].joinpath('data')


def readData(filename: str) -> List[dict]:
    with open(__LOCAL.joinpath(filename)) as dataJson:
        serializedObject = json.load(dataJson)

    return serializedObject
