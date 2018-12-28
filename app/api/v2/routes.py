"""all for version 2 routes"""
from flask import Blueprint
from flask_restful import Api

from .users.views import UserSignUp, UserSignIn, Users, Search, UserStatus
from .incidents.views_interventions import (Interventions, Intervention, UpdateInterventionLocation,
                              UpdateInterventionComment, UpdateInterventionStatus)
from .incidents.views_redflags import (
    Redflags, Redflag, UpdateRedflagLocation, UpdateRedflagComment, UpdateRedflagStatus)

VERSION_TWO = Blueprint('apiv2', __name__, url_prefix='/api/v2')
API = Api(VERSION_TWO)

API.add_resource(UserSignUp, '/auth/signup')
API.add_resource(UserSignIn, '/auth/signin')
API.add_resource(Users, '/users')
API.add_resource(Search, '/users/<string:email>')
API.add_resource(UserStatus, '/users/<string:email>/status')
API.add_resource(Interventions, '/interventions')
API.add_resource(Intervention, '/intervention/<int:incident_id>')
API.add_resource(UpdateInterventionLocation,
                 '/interventions/<int:incident_id>/location')
API.add_resource(UpdateInterventionComment,
                 '/interventions/<int:incident_id>/comment')
API.add_resource(UpdateInterventionStatus,
                 '/interventions/<int:incident_id>/status')
API.add_resource(Redflags, '/redflags')
API.add_resource(Redflag, '/redflag/<int:incident_id>')
API.add_resource(UpdateRedflagLocation,
                 '/redflags/<int:incident_id>/location')
API.add_resource(UpdateRedflagComment,
                 '/redflags/<int:incident_id>/comment')
API.add_resource(UpdateRedflagStatus, '/redflags/<int:incident_id>/status')
