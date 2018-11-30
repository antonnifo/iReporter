from flask import Blueprint
from flask_restful import Api, Resource
from .redflags.views import RedFlags, RedFlag, UpdateLocation

version1= Blueprint('api',__name__,url_prefix='/api/v1')
api=Api(version1)

api.add_resource(RedFlags, '/red-flags') 
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
api.add_resource(UpdateLocation, '/red-flags/<int:redflag_id>/location')