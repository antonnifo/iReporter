from flask import Blueprint
from flask_restful import Api, Resource

from .redflags.views import RedFlags

version1= Blueprint('api',__name__,url_prefix='/api/v1')
api=Api(version1)

api.add_resource(RedFlags, '/red-flags') 
