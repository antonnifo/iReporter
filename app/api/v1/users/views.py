"""Views for users"""
from flask_restful import Resource
from flask import jsonify, make_response
from app.api.v1.users.models import UserModel


class Users(Resource):
    """docstring for users"""

    def __init__(self):
        self.db = UserModel()

    def post(self):
        """method to post a user"""
        user_id = self.db.save_user()

        if user_id == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError for email/password not posted"
            }), 500)

        if user_id == "email exists":
            return make_response(jsonify({
                "status": 400,
                "error": "email already exists"
            }), 400)

        if user_id == "username exists":
            return make_response(jsonify({
                "status": 400,
                "error": "username already exists"
            }), 400)

        success_message = {
            "id": user_id,
            "message": "Created user record"
        }

        return make_response(jsonify({
            "status": 201,
            "data": success_message
        }), 201)
