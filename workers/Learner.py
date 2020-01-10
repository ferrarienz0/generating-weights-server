# Custom imports
from pandas import DataFrame

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from numpy import unique


def __getTrainedDatasets(dataframe: DataFrame, features: list, target: list) -> tuple:
    X = dataframe[features]
    y = dataframe[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=101)

    return X_train, X_test, y_train, y_test


def getModelAndClassification(dataframe: DataFrame, features: list, target: list) -> tuple:
    model: LogisticRegression = LogisticRegression()

    X_train, X_test, y_train, y_test = __getTrainedDatasets(
        dataframe, features, target)

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    classification = classification_report(
        y_test, predictions, zero_division=0)

    return model, classification
