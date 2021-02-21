# Native imports
from typing import List
from json import load

# Custom imports
from workers import Inputter
from workers import Treatter
from workers import Learner
from workers import Plotter

from pandas import DataFrame

# Chama as funções necessárias para
# executar o algoritmo


def runProcess(data: dict) -> tuple:
    # Extrai as features dos dados passados via requisição
    # POST. As features são as notas dos critérios, é com
    # base nelas que os pesos são calculados
    features = Treatter.getFeatures(data)

    # A target é a variável de destino, os pesos serão utilizados
    # para tentar prever a variável target
    target = 'success'

    # Aqui os dados são convertidos para a estrutura de dados utilizada
    # pela biblioteca Pandas e Scikit-Learn
    dataFrame = Treatter.createDataFrame(data)

    # Aqui é feita a chamada à função de regressão logística e obtém tanto
    # o modelo gerado quanto o resultado bruto da predição.
    model, classification = Learner.getModelAndClassification(
        dataFrame, features, target)

    # Aqui é criado o objeto final que será retornado ao usuário.
    # São passados os coeficientes (pesos) obtidos na função anterior,
    # o limite inferior e superior e as features
    finalMap = Treatter.createFinalMap(model.coef_[0], 1, 9, features)

    # Aqui são plotados os gráficos
    Plotter.plotMap(finalMap)

    return finalMap, classification
