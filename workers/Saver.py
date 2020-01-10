# Native imports
from typing import List
from json import load
from pathlib import Path
from os import getenv

# Custom imports
from pymongo import MongoClient
from dotenv import load_dotenv

__ENV_PATH = Path(__file__).parents[1] / '.env'

load_dotenv(dotenv_path=__ENV_PATH)

__MONGOADDRESS = getenv('MONGO_ADDRESS')
__CLIENT = MongoClient(__MONGOADDRESS)
__DB = __CLIENT['cimatec']
__COLLECTION = __DB['calls']


def sendCallToDatabase(document: dict) -> bool:
    result = __DB['calls'].insert_one(document)

    return result.inserted_id != None


def sendProcessedWeitghsToDatabase(document: dict) -> bool:
    result = __DB['processedWeights'].insert_one(document)

    return result.inserted_id != None


def getFromDB(collection: str) -> list:
    result = __DB[collection].find({})

    response: list = []

    for call in result:
        response.append(call)

    return list(response)
