"""Views for users"""
import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource

import jwt
from .models import UserModel


class UserSignUp(Resource):
    """Class with user signup post method"""

    def __init__(self):
        self.db = UserModel()

    def post(self):
        """method to post user details"""
        user = self.db.save()

        if user == "email already exists":
            return make_response(jsonify({
                "status": 400,
                "error": "email already exists"
            }), 400)
        return make_response(jsonify({
            "status": 201,
            "data": [
                {
                    "user": user,
                    "message": "Account created"
                }
            ]
        }), 201)

class UserSignIn(Resource):
    """Class containing user login method"""

    def __init__(self):
        self.db = UserModel()

    def post(self):
        """method to get a specific user"""
        user = self.db.log_in()
        if user == None:
            return make_response(jsonify({
                "status": 200,
                "message": "user does not exist"
            }), 200)
        if user == 'invalid password':
            return make_response(jsonify({
                "status": 200,
                "message": "password is incorrect"
            }), 200)

        
        return make_response(jsonify({
            "status": 200,
            "data": [
                {
                    "user": user
                }
            ]
        }), 200)        

class Users(Resource):
    """Class with methods for dealing with all users"""

    def __init__(self):
        self.db = UserModel()

    def get(self):
        """method to get all users"""
        return make_response(jsonify({
            "status": 200,
            "data": self.db.find_users()
        }), 200)