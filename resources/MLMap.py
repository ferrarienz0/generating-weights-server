# Native imports
from copy import deepcopy
from json import load

# Custom imports
from flask import request
from flask import jsonify
from flask_restful import Resource

from mainProcess import runProcess

from workers import Saver


class MLMap(Resource):
    def post(self):
        data = request.get_json(force=True)

        toSend = deepcopy(data)

        dbStatus: bool = Saver.sendCallsToDatabase(toSend)

        return jsonify({'data': data, 'saved': dbStatus})

    def get(self):
        data = Saver.getFromDB('calls')

        finalMap, classification = runProcess(data)

        response: dict = {'finalMap': finalMap,
                          'classification': classification}

        document = deepcopy(response)

        dbStatus: bool = Saver.sendProcessedWeitghsToDatabase(document)

        response['saved'] = dbStatus

        return jsonify(response)
