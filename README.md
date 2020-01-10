# generating-weights

Register calls from the cimatec accelerator. The server also run a logistic regression based on the stored calls to help improve the weight-criteria system.

## Getting Started

```
After cloning this repository, create a .env file containing the mongoDB service URL and the server port.

Install virtualenv using:
(Windows) **py -m pip install --user virtualenv**
(Linux) **python3 -m pip install --user virtualenv**

Create virtualenv using:
(Windows) **py -m venv env**
(Linux) **python3 -m venv env**

Active the virtualenviromment using:
(Windows) **.\env\Scripts\activate**
(Linux) **source env/bin/activate**

Install pre-requisits with pip:
(Windows) **pip install -r requirements.txt**
(Linux) **pip3 install -r requirements.txt**

(The version used for python was 3.6.9)

Run with:
(Windows) **py server.py**
(Linux) **python3 server.py**
```

## API

```
There is only one route, '/'.

GET requisition -> Returns the map, result of the logistic regression analysis on stored data and it's evaluation.
POST requisition -> Need a JSON Body (see example.JSON), stores a call in the database
```

## Built with

- [Python](https://www.python.org/)
- [Flask](https://palletsprojects.com/p/flask/)
- [SKlearn](https://scikit-learn.org/stable/)
