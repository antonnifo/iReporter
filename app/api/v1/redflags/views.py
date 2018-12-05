"""views for Red-flags"""
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
        redflag_id = self.db.save()

        if redflag_id == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError for createdBy Red-flag not posted"
            }), 500)

        return make_response(jsonify({
            "status": 201,
            "data": {
                "id": redflag_id,
                "message": "Created red-flag record"
            }
        }), 201)

    def get(self):
        """docstring for getting all the redflags posted"""
        self.db.get_all()
        return make_response(jsonify({
            "status": 200,
            "data": self.db.get_all()
        }), 200)


class RedFlag(Resource):
    """docstring of a single RedFlag"""

    def __init__(self):
        """initiliase the Redflag class"""
        self.db = RedFlagModel()

    def get(self, redflag_id):
        """docstring for getting a specific red-flag"""
        incident = self.db.find(redflag_id)
        if incident == "red flag does not exit":
               return make_response(jsonify({
                    "status": 404,
                    "error": "red flag does not exit"
                }), 404)
       
        return make_response(jsonify({
            "status": 200,
            "data": incident
        }), 200)

    def delete(self, redflag_id):
        """docstring for deleting a red-flag"""
        incident = self.db.find(redflag_id)
        if incident == "red flag does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "red flag does not exit"
            }), 404)
        delete_status = self.db.delete(incident)
        if delete_status == "deleted":
            return make_response(jsonify({
                "status": 200,
                "data": 'red-flag record has been deleted'
            }), 200)

    def put(self, redflag_id):
        """docstring for updating  redflag record"""
        incident = self.db.find(redflag_id)
        if incident == "red flag does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "red flag does not exit"
            }), 404)
        edit_status = self.db.edit_redflag(incident)
        if edit_status == "updated":
            return make_response(jsonify({
                "status": 200,
                "data": {
                    "id": redflag_id,
                    "message": "Red-flag has been updated"
                }
            }))


class UpdateLocation(Resource):
    """class to update redflag location"""

    def __init__(self):
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        """method to update redflag location"""
        incident = self.db.find(redflag_id)

        if incident == "red flag does not exist":
            return make_response(jsonify({
                "status": 404,
                "error": "Red-flag does not exist"
            }), 404)
        edit_status = self.db.edit_redflag_location(incident)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError Red-flag's location not updated"
            }), 500)
        elif edit_status == "updated":
            return make_response(jsonify({
                "status": 200,
                "data": {
                    "id": redflag_id,
                    "message": "Updated red-flag record's location"
                }
            }), 200)


class UpdateComment(Resource):
    """docstring for patching comment"""

    def __init__(self):
        self.db = RedFlagModel()

    def patch(self, redflag_id):
        """method to update comment in a redflag"""
        incident = self.db.find(redflag_id)

        if incident == "red flag does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "red flag does not exit"
            }), 404)

        edit_status = self.db.edit_redflag_comment(incident)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError Red-flag's comment not updated"
            }), 500)
        elif edit_status == "updated":
            return make_response(jsonify({
                "status": 200,
                "data": {
                    "id": redflag_id,
                    "message": "Updated red-flag record's comment"
                }
            }), 200)
