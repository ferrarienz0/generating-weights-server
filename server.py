# Native imports
from os import getenv

# Custom imports
from resources.MLMap import MLMap
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv

__APP = Flask(__name__)
__CORS = CORS(__APP)
__APP.config['CORS_HEADERS'] = 'Content-Type'
__API = Api(__APP)

__API.add_resource(MLMap, '/')

# Carrega as informações de HOST e porta
# das variáveis de ambiente
load_dotenv()
__HOST = getenv('HOST')
__PORT = getenv('PORT')

# Inicia o servidor
if __name__ == '__main__':
    __APP.run(host=__HOST, port=__PORT, debug=True)
