import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource

from .models import RedFlagModel


class RedFlags(Resource):
    """docstring for RedFlags class"""
    def __init__(self):
        """initiliase the redflag class"""    
        self.db = RedFlagModel()

    def post(self):
        """docstring for saving a redflag"""            
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

    def get(self):
        """docstring for getting all the redflags posted"""    
        self.db.get_all()      
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200) 

class RedFlag(Resource):
    """docstring of a single RedFlag"""
    def __init__(self):
        """initiliase the Redflag class"""    
        self.db = RedFlagModel()
        
    def get(self, redflag_id):
        """docstring for getting a specific red-flag"""    
        incident = self.db.find(redflag_id)
        return make_response(jsonify({
                    "status" : 200,
                    "data" : incident
                }), 200)
      
    def delete(self, redflag_id):
        """docstring for deleting a red-flag"""    
        incident = self.db.find(redflag_id)
        self.db.delete(incident)
        success_message = {
                'message' : 'red-flag record has been deleted'
                 }
        return make_response(jsonify({
                "status" : 204,
                "data" : success_message
                }))  

    def put(self, redflag_id):
        """docstring for updating any of the records posted"""    
        incident = self.db.find(redflag_id)
        if incident:
                incident['createdBy'] = request.json.get('createdBy', incident['createdBy'])
                incident['location'] = request.json.get('location', incident['location'])
                incident['images'] = request.json.get('images', incident['images'])
                incident['videos'] = request.json.get('videos', incident['videos'])
                incident['title'] = request.json.get('title', incident['title'])
                incident['comment'] = request.json.get('comment', incident['comment'])

                success_message = {
                    "message" : "Red-flag has been updated"
                }

                return make_response(jsonify({
                    "status" : 201,
                    "data" : success_message
                }), 201)


class UpdateLocation(Resource):
    """docstring of editing Location"""
    def __init__(self):
        """initiliase the updatelocation class"""    
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        """docstring of editing a specific Location"""    
        incident = self.db.find(redflag_id)
        if incident:
            incident['location'] = request.json.get('location', incident['location'])
            success_message = {
                        "message" : "Updated red-flag record's location"
                    }
            return make_response(jsonify({
                "status" : 201,
                "data" : success_message
            }), 201)  

class UpdateComment(Resource):
    """docstring of editing comment"""
    def __init__(self):
        """initiliase the updatecomment class"""     
        self.db = RedFlagModel()
    def patch(self, redflag_id):
        """docstring of editing comment"""    
        incident = self.db.find(redflag_id)
        if incident:
                incident['comment'] = request.json.get('comment', incident['comment'])
                success_message = {
                    "message" : "Updated red-flag record's comment"
                }
                return make_response(jsonify({
                    "status" : 201,
                    "data" : success_message
                }), 201)                                                             
