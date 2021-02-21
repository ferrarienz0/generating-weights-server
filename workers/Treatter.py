# Native imports
from typing import List
from typing import Dict

# Custom imports
from pandas import DataFrame


def getFeatures(data: dict) -> list:
    features: list = list()

    for data_ in data:
        for criteria in data_['criteria']:
            if criteria['name'] not in features:
                features.append(criteria['name'])

    return features


def __prepareDict(data: list) -> list:
    for data_ in data:
        criteriaInfo = data_['criteria']

        for criteria in criteriaInfo:
            data_[criteria['name']] = criteria['score']

        del data_['criteria']

    return data

# Aqui os coeficientes são tratados para se adequar ao range especificado
# A regressão logarítmica pode retornar ranges diversos, e portanto, é
# necessário colocá-los no especificado.


def __treatCoefficients(coefficients: list, lowerLimit: int, higherLimit: int) -> list:
    sortedCoefficients = sorted(coefficients)

    oldRange = sortedCoefficients[0] - \
        sortedCoefficients[len(sortedCoefficients) - 1]

    newRange = higherLimit - lowerLimit

    treatedCoefficients: list = []

    for x in range(len(coefficients)):
        distance = abs(coefficients[x] - sortedCoefficients[0])

        value = (distance * newRange / oldRange) - 1

        treatedCoefficients.append(int(round(value)))

    return treatedCoefficients

# Aqui é feita a etapa de relação das features
# com os pesos encontrados


def __relateCoefficients(features: list, coefficientMap: List[list]) -> Dict[str, dict]:
    coefficientDict: dict = {}

    for (index, row) in enumerate(coefficientMap):
        rowDict: dict = {}

        for (index_, column) in enumerate(row):
            relatedFeature = features[index_ + index + 1]

            rowDict[relatedFeature] = column

        coefficientDict[features[index]] = rowDict

    return coefficientDict

# Aqui os coeficientes são relacionados
# por distância, para se encontrarem
# no range de -9 a 9.


def __generateCoefficientMap(coefficients: list) -> List[list]:
    coefficientMap: List[list] = []

    for x in range(len(coefficients) - 1):
        normalizedCoefficients: list = []

        for y in range(x + 1, len(coefficients)):
            distance = coefficients[x] - coefficients[y]

            if distance < 0:
                distance -= 1

            else:
                distance += 1

            normalizedCoefficients.append(distance)

        coefficientMap.append(normalizedCoefficients)

    return coefficientMap


def createDataFrame(data: list) -> DataFrame:
    preparedDict = __prepareDict(data)

    index = [x['name'] for x in preparedDict]

    for x in preparedDict:
        del x['name']

    return DataFrame(preparedDict, index=index)

# O objeto final é retornado contendo a relação das
# features com os pesos de outros critérios.


def createFinalMap(coefficients: list, lowerLimit: int, higherLimit: int, features) -> Dict[str, dict]:
    treatedCoefficitents = __treatCoefficients(
        coefficients, lowerLimit, higherLimit)

    coefficientMap = __generateCoefficientMap(treatedCoefficitents)

    finalMap = __relateCoefficients(features, coefficientMap)

    return finalMap
