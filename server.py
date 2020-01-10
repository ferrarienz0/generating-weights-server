# Native imports
from os import getenv

# Custom imports
from resources.MLMap import MLMap
from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv

__APP = Flask(__name__)
__API = Api(__APP)


__API.add_resource(MLMap, '/')

load_dotenv()

if __name__ == '__main__':
    __APP.run(host=getenv('HOST'), port=getenv('PORT'), debug=True)
