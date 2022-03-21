from flask import jsonify
from flask import request
from flask_restful import Resource
from datetime import datetime


# Hardcoded data

users = [
    {"id": 1, "firstName": 'Andre', "lastName": 'R'},
    {"id": 2, "firstName": 'Test', "lastName": 'Dupont'},
]

# /users routes
class UsersApi(Resource):
    def get(self):
        # The jsonify module will transforms python
        # dict to JSON objects (not needed for strings, numbers)
        return jsonify(users)

    def delete(self):
        users.clear()
        return jsonify(users)

    def post(self):
        body = request.json
        new_user = { 
            "id": body["id"],
            "firstName": body['firstName'],
            "lastName": body['lastName'],
        }
        users.append(new_user)
        return jsonify(users)

# /users/<userId> routes
class UserApi(Resource):
    def get(self, userId):
        # filters the users and get the first item with next
        found = next(filter(lambda u: u["id"] == int(userId), users), None)
        if found == None:
            return {'error': 'User with id %s not found' % userId}, 404
        return jsonify(found)

    def delete(self, userId):
        for i in range(len(users)): 
            if users[i]['id'] == userId: 
                del users[i] 
                break
        return jsonify(users)


