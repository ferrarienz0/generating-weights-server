# generating-weights

Register calls from the cimatec accelerator. The server also run a logistic regression based on the stored calls to help improve the weight-criteria system.

## Getting Started

After cloning this repository, create a .env file containing the mongoDB service URL, the server port and host (see .env.example).

Install virtualenv using: <br />
(Windows) **py -m pip install --user virtualenv** <br />
(Linux) **python3 -m pip install --user virtualenv**

Create virtualenv using: <br />
(Windows) **py -m venv env** <br />
(Linux) **python3 -m venv env**

Active the virtualenviromment using: <br />
(Windows) **.\env\Scripts\activate** <br />
(Linux) **source env/bin/activate**

Install requirements with pip: <br />
(Windows) **pip install -r requirements.txt** <br />
(Linux) **pip3 install -r requirements.txt**

(The version used for python was 3.6.9)

Run with: <br />
(Windows) **py server.py** <br />
(Linux) **python3 server.py**

## API

There is only one route, '/'.

GET requisition -> Returns the map, result of the logistic regression analysis on stored data and it's evaluation. <br />
Example response:

```
{
  "classification": {
    "0": {
      "f1-score": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "support": 0.0
    },
    "1": {
      "f1-score": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "support": 2.0
    },
    "accuracy": 0.0,
    "macro avg": {
      "f1-score": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "support": 2.0
    },
    "weighted avg": {
      "f1-score": 0.0,
      "precision": 0.0,
      "recall": 0.0,
      "support": 2.0
    }
  },
  "finalMap": {
    "empreendedor e equipe": {
      "viabilidade de negócio": -9
    }
  },
  "saved": true
}
```

POST requisition -> Need a JSON Body (see example.JSON), stores a call in the database <br />
Example Body:

```
{
    "name": "bioenergia",
    "criteria": [
      {
        "name": "empreendedor e equipe",
        "score": 0
      },
      {
        "name": "viabilidade de negócio",
        "score": 1
      }
    ],
    "sucess": 1
  }
```

## Built with

- [Python](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [SKlearn](https://scikit-learn.org/stable/)
- [Matplotlib](https://matplotlib.org/)
