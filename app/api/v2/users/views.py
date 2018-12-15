"""Views for users"""
import os
import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource

import jwt
from .models import UserModel

secret = os.getenv('SECRET_KEY')


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
        payload = {
            "email": user['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload=payload, key=secret, algorithm='HS256')
        return make_response(jsonify({
            "status": 201,
            "data": [
                {
                    "account details": user,
                    "token": token.decode('UTF-8'),
                    "message":"You have created an account.sign in"
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
        if user == 'incorrect password':
            return make_response(jsonify({
                "status": 200,
                "message": "password is incorrect please try again"
            }), 200)

        payload = {
            "email": user,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload=payload, key=secret, algorithm='HS256')
        return make_response(jsonify({
            "status": 200,
            "data": [
                {
                    "token": token.decode('UTF-8'),
                    "user": user,
                    "message":"You are now signed in you can post an incident"
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


class Search(Resource):
    """docstring filtering incidents by type"""

    def __init__(self):
        """initiliase the incident class"""
        self.db = UserModel()

    def get(self, email):
        """method for getting a specific user by email"""
        user = self.db.find_user_by_email(email)
        if user == None:
            return make_response(jsonify({
                "status": 404,
                "error": "user does not exit"
            }), 404)

        return make_response(jsonify({
            "status": 200,
            "data": user
        }), 200)
