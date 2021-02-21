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
    # Função que é chamada quando uma requisição
    # POST é feita. Os dados são salvos no banco
    # de dados para posterior análise.
    def post(self):
        data = request.get_json(force=True)

        toSend = deepcopy(data)

        dbStatus: bool = Saver.sendCallToDatabase(toSend)

        return jsonify({'data': data, 'saved': dbStatus})

    # Função que é chamada quando uma requisição
    # GET é feita. Aqui é puxado o histórico do
    # banco de dados para executar o processo de
    # geração de pesos
    def get(self):
        data = Saver.getFromDB('calls')

        if len(data) == 0 or data == None:
            return jsonify({'message': 'There is no call stored yet, ML process cannot run'})

        finalMap, classification = runProcess(data)

        response: dict = {'result': finalMap,
                          'classification': classification}

        document = deepcopy(response)

        dbStatus: bool = Saver.sendProcessedWeitghsToDatabase(document)

        response['saved'] = dbStatus

        return jsonify(response)
