# Custom imports
from resources.MLMap import MLMap
from flask import Flask
from flask_restful import Api

__APP = Flask(__name__)
__API = Api(__APP)


__API.add_resource(MLMap, '/')

if __name__ == '__main__':
    __APP.run(host='0.0.0.0', port=3000, debug=True)
