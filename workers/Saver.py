# Native imports
from typing import List
from json import load

# Custom imports
from pymongo import MongoClient

__CLIENT = MongoClient()
__DB = __CLIENT['cimatec']
__COLLECTION = __DB['calls']


def sendCallsToDatabase(document: List[dict]) -> bool:
    result = __DB['calls'].insert_many(document, ordered=False)

    return result.inserted_ids != None


def sendProcessedWeitghsToDatabase(document: dict) -> bool:
    result = __DB['processedWeights'].insert_one(document)

    return result.inserted_id != None


def getFromDB(collection: str) -> list:
    result = __DB[collection].find({})

    response: list = []

    for call in result:
        response.append(call)

    return list(response)
