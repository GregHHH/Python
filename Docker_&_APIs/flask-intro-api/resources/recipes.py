from flask import jsonify
from flask import request
from flask_restful import Resource
from datetime import datetime, date
import requests
import json 

## Path vers le dossier service
# from service import *

api_url = "http://146.59.225.32"
today = date.today()

# /recipes routes
class RecipesApi(Resource):
	def get(self):
		response = requests.get(url = api_url + '/recipes')
		recipes = response.json()
		return jsonify(recipes)

	def delete(self):
		## add verif
		return jsonify(recipes)

	def post(self):
		responses = requests.request("POST", auth_url, headers = headers, data = payload)
		print(responses.json)

		date_now = today.strftime("%d/%m/%Y")
		body = request.json
		new_recipe = { 
			"name": body["name"],
			"description": body["description"],
			# "published_at": str(date_now),
			# "created_at": str(date_now),
			# "updated_at": str(date_now),
			# "preview": null,
			"chefs": body["chefs"]
		}
		recipes.append(new_recipe)
		response = requests.post(url = api_url + '/recipes', params=new_recipe)
		result = responses.json()
		return jsonify(result)

# /recipes/<recipesId> routes
class RecipeApi(Resource):
	def get(self, recipesId):
		response = requests.get(url = api_url + '/recipes/' + recipesId)
		if response == None:
			return {'error' : 'Recipe with id %s not found' % recipesId}, 404
		result = response.json()
		return jsonify(result)


