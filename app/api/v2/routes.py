"""all for version 2 routes"""
from flask import Blueprint
from flask_restful import Api

from .users.views import  UserSignUp

VERSION_TWO = Blueprint('apiv2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(UserSignUp, '/auth/signup')
