from pandas import DataFrame


def getFeatures(data: dict) -> list:
    features: set = set()

    for data_ in data:
        for criteria in data_['criteria']:
            features.add(criteria['name'])

    return features


def __prepareDict(data: list) -> list:
    for data_ in data:
        criteriaInfo = data_['criteria']

        for criteria in criteriaInfo:
            data_[criteria['name']] = criteria['score']

        del data_['criteria']

    return data


def createDataFrame(data: list) -> DataFrame:
    preparedDict = __prepareDict(data)

    index = [x['name'] for x in preparedDict]

    for x in preparedDict:
        del x['name']

    return DataFrame(preparedDict, index=index)
