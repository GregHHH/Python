from flask import Flask
from flask import jsonify
from flask_restful import Api
from resources.users import UsersApi, UserApi
from resources.recipes import RecipesApi, RecipeApi
from resources.chefs import ChefsApi, ChefApi

app = Flask(__name__, instance_relative_config=True)

app.config['PROPAGATE_EXCEPTIONS'] = True

# Loads configuration from config.py
app.config.from_object('config')
## From here you can access config variables like this:
## value_from_config = app.config['CONFIG_VARIABLE_NAME']

## Initialisation des modules 

api = Api(app)

## Declaration of API routes

api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/users/<userId>')
api.add_resource(RecipesApi, '/recipes')
api.add_resource(RecipeApi, '/recipes/<recipesId>')
api.add_resource(ChefsApi, '/chefs')
api.add_resource(ChefApi, '/chefs/<chefsId>')

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello World"})

