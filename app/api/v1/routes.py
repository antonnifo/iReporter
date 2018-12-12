"""all routes"""
from flask import Blueprint
from flask_restful import Api

from .redflags.views import RedFlag, RedFlags, UpdateComment, UpdateLocation

VERSION_UNO = Blueprint('api', __name__, url_prefix='/api/v1')
API = Api(VERSION_UNO)
API.add_resource(RedFlags, '/red-flags')
API.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
API.add_resource(UpdateLocation, '/red-flags/<int:redflag_id>/location')
API.add_resource(UpdateComment, '/red-flags/<int:redflag_id>/comment')
