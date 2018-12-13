"""all for version 2 routes"""
from flask import Blueprint
from flask_restful import Api

from .users.views import UserSignUp, UserSignIn, Users
from .incidents.views import Incidents, Incident, UpdateLocation, UpdateComment, UpdateStatus, Filter

VERSION_TWO = Blueprint('apiv2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(UserSignUp, '/auth/signup')
API.add_resource(UserSignIn, '/auth/signin')
API.add_resource(Users, '/users')
API.add_resource(Incidents, '/incidents')
API.add_resource(Incident, '/incidents/<int:incident_id>')
API.add_resource(Filter, '/incidents/<string:incident_type>')
API.add_resource(UpdateLocation, '/incidents/<int:incident_id>/location')
API.add_resource(UpdateComment, '/incidents/<int:incident_id>/comment')
API.add_resource(UpdateStatus, '/incidents/<int:incident_id>/status')
