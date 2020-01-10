# Native imports
from typing import List
from json import load

# Custom imports
from workers import Inputter
from workers import Treatter
from workers import Learner
from workers import Plotter

from pandas import DataFrame


def runProcess(data: dict) -> tuple:
    features = Treatter.getFeatures(data)
    target = 'sucess'

    dataFrame = Treatter.createDataFrame(data)

    model, classification = Learner.getModelAndClassification(
        dataFrame, features, target)

    finalMap = Treatter.createFinalMap(model.coef_[0], 1, 9, features)

    # plots: list = Plotter.plotMap(finalMap)

    return finalMap, classification
