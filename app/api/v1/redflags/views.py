from flask_restful import Resource
from flask import jsonify, make_response, request
from .models import RedFlagModel
import datetime


class RedFlags(Resource):
    """docstring for RedFlags"""
    
    def __init__(self):
        self.db = RedFlagModel()

    def post(self):
        
        data = {
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json.get('createdBy', ""),
            'type' : 'red-flags',
            'location' : request.json.get('location', ""),
            'status' : "Under Invsetigation",
            'images' : request.json.get('images', ""),
            'videos' : request.json.get('videos', ""),
            'title' : request.json['title'],
            'comment' : request.json.get('comment', "")
        }
        self.db.save(data)
        
        success_message = {
            'message' : 'Created red-flag record'
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_message
        }), 201)    