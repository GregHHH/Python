from flask import Flask
from flask import jsonify
from flask_restful import Api
from resources.users import UsersApi, UserApi

app = Flask(__name__, instance_relative_config=True)

app.config['PROPAGATE_EXCEPTIONS'] = True

# Loads configuration from config.py
app.config.from_object('config')

## Initialisation des modules 

api = Api(app)

## Declaration of API routes

api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/users/<userId>')

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"})
