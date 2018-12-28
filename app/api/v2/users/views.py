"""Views for users"""
import os
import datetime

from flask import jsonify,request
from flask_restful import Resource
from app.api.v2.token_decorator import require_token
from app.api.v2.validators import only_admin_can_edit
import jwt
from .models import UserModel

secret = os.getenv('SECRET_KEY')

def nonexistent_user():
    return jsonify({
        "status": 404,
        "message": "user does not exist"
    })

def admin_user():
    return jsonify({
        "status": 403,
        "message": "Only admin can access this route"
    })

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
            "name": user['first_name']+' '+user['last_name'],
            "email": user['email'],
            "phone": user['phone']

        }
        return jsonify({
            "status": 201,
            "data": [
                {
                    "account details": user_details,
                    "token": token.decode('UTF-8'),
                    "message": "You have created an account you can now post incidents"
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
            return nonexistent_user()

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
                    "message": "You are now signed in you can post an incident"
                }
            ]
        })


class Users(Resource):
    """Class with methods for dealing with all users"""

    def __init__(self):
        self.db = UserModel()

    @require_token
    def get(current_user, self):
        """method to get all users"""
        if current_user['isadmin'] is False:
            return admin_user() 

        return jsonify({
            "status": 200,
            "data": self.db.find_users()
        })


class Search(Resource):
    """docstring filtering incidents by type"""

    def __init__(self):
        """initiliase the incident class"""
        self.db = UserModel()
    
    @require_token
    def get(current_user, self, email):
        """method for getting a specific user by email"""
        if current_user['isadmin'] is False:
            return admin_user()

        user = self.db.find_user_by_email(email)
        if user is None:
            return nonexistent_user()

        user_details = {
            "name": user['first_name']+' '+user['last_name'],
            "email": user['email'],
            "phone": user['phone'],
            "regestered":user['registered'],
            "isAdmin":user['isadmin']
        }
        return jsonify({
            "status": 200,
            "data": user_details
        })

    @require_token
    def delete(current_user, self, email):
        """method to delete a user"""

        user = self.db.find_user_by_email(email)
        if user is None:
            return nonexistent_user()

        if current_user['isadmin'] is not True:
            return jsonify({
                "status": 403,
                "message": "Only an admin can delete a user"
            })

        delete_status = self.db.delete_user(email)
        if delete_status is True:

            return jsonify({
                "status": 200,
                "data": {
                    "email": email,
                    "message": "user record has been deleted"
                }
            })


class UserStatus(Resource):
    """Class with method for updating a  specific user admin status"""

    def __init__(self):
        self.db = UserModel()

    @require_token
    def patch(current_user, self, email):
        """method to promote a user"""
        user = self.db.find_user_by_email(email)
        if user is None:
            return nonexistent_user()

        if current_user['isadmin'] is not True:
            return jsonify({
                "status": 403,
                "message": "Only an admin can change the status of a user"
            })

        user_status_updated = self.db.edit_user_status(email)
        if user_status_updated is True:
            success_message = {
                "email": email,
                "message": "User status has been updated"
            }
            return jsonify({
                "status": 200,
                "data": success_message
            })