"""all routes"""
from flask import Blueprint
from flask_restful import Api

from .redflags.views import RedFlag, RedFlags, UpdateComment, UpdateLocation
from .users.views import UpdateUserPassword, UpdateUserStatus, User, Users

VERSION_UNO = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_UNO)
API.add_resource(RedFlags, '/red-flags')
API.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
API.add_resource(UpdateLocation, '/red-flags/<int:redflag_id>/location')
API.add_resource(UpdateComment, '/red-flags/<int:redflag_id>/comment')

API.add_resource(Users, '/users')
API.add_resource(User, '/users/<int:user_id>')
API.add_resource(UpdateUserPassword, '/users/<int:user_id>/password')
API.add_resource(UpdateUserStatus, '/users/<int:user_id>/status')
