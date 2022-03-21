from flask import jsonify
from flask import request
from flask_restful import Resource
from datetime import datetime, date
import requests

api_url = "http://146.59.225.32"


# /chefs routes
class ChefsApi(Resource):
	def get(self):
		response = requests.get(url = api_url + '/chefs')
		result = response.json()
		return jsonify(result)

class ChefApi(Resource):
	def get(self, chefsId):
		response = requests.get(url = api_url + '/chefs/' + chefsId)
		if response == None:
			return {'error': 'Recipe with id %s not found' % chefsId}, 404
		result = response.json()
		return jsonify(result)