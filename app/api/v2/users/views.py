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
            return jsonify({
                "status": 400,
                "error": "email already exists"
            })
        payload = {
            "email": user['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload=payload, key=secret, algorithm='HS256')

        user_details = {
                    "name" : user['first_name']+' '+user['last_name'],
                    "email" : user['email'],
                    "phone" : user['phone']

        }
        return jsonify({
            "status": 201,
            "data": [
                {
                    "account details": user_details,
                    "token": token.decode('UTF-8'),
                    "message":"You have created an account you can now post incidents"
                }
            ]
        })


class UserSignIn(Resource):
    """Class containing user login method"""

    def __init__(self):
        self.db = UserModel()

    def post(self):
        """method to get a specific user"""
        user = self.db.log_in()
        if user is None:
            return jsonify({
                "status": 404,
                "message": "user does not exist"
            })
        if user == 'incorrect password':
            return jsonify({
                "status": 401,
                "message": "password or email is incorrect please try again"
            })

        payload = {
            "email": user,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload=payload, key=secret, algorithm='HS256')
        
        return jsonify({
            "status": 200,
            "data": [
                {
                    "token": token.decode('UTF-8'),
                    "user": user,
                    "message":"You are now signed in you can post an incident"
                }
            ]
        })


class Users(Resource):
    """Class with methods for dealing with all users"""

    def __init__(self):
        self.db = UserModel()

    def get(self):
        """method to get all users"""
        return jsonify({
            "status": 200,
            "data": self.db.find_users()
        })


class Search(Resource):
    """docstring filtering incidents by type"""

    def __init__(self):
        """initiliase the incident class"""
        self.db = UserModel()

    def get(self, email):
        """method for getting a specific user by email"""
        user = self.db.find_user_by_email(email)
        if user == None:
            return jsonify({
                "status": 404,
                "error": "user does not exit"
            })

        return jsonify({
            "status": 200,
            "data": user
        })
