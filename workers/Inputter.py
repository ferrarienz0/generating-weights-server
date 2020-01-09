from typing import List
from pathlib import Path
import json

from processDefinitions import Call

LOCAL = Path(__file__).parents[1].joinpath('data')

print(LOCAL)


def readAndConvertJSON(filename: str) -> List[Call]:
    serializedObject = __readData(filename)

    return __getCalls(serializedObject)


def __readData(filename: str) -> List[dict]:
    with open(LOCAL.joinpath(filename)) as dataJson:
        serializedObject = json.load(dataJson)

    return serializedObject


def __getCalls(serializedObject: List[dict]) -> List[Call]:
    calls: List[Call] = [Call(x) for x in serializedObject]

    return calls
