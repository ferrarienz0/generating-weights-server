# Native imports
from typing import List

# Custom imports
from workers import Inputter
from workers import Treatter
from workers import Learner

data = Inputter.readData('data.json')

features = Treatter.getFeatures(data)
target = 'sucess'

dataFrame = Treatter.createDataFrame(data)

model, classification = Learner.getModelAndClassification(
    dataFrame, features, target)

print(classification)
