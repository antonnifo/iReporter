"""Views for Interventions"""
import datetime

from flask import jsonify, make_response, request, session
from flask_restful import Resource

from .models import IncidentModel


class Incidents(Resource):
    """docstring for incidents class"""

    def __init__(self):
        """initiliase the incidents class"""
        self.db = IncidentModel()

    def post(self):
        """docstring for saving an incident"""
        incidents_id = self.db.save()

        if incidents_id is "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError for createdBy incident not posted"
            }), 500)

        return make_response(jsonify({
            "status": 201,
            "data": {
                "id": incidents_id,
                "message": "Created incidents record"
            }
        }), 201)

    def get(self):
        """docstring for getting all the incidents posted by users"""
        self.db.find_all()
        return make_response(jsonify({
            "status": 200,
            "data": self.db.find_all()
        }), 200)


class Incident(Resource):
    """docstring of a single incident"""

    def __init__(self):
        """initiliase the incident class"""
        self.db = IncidentModel()

    def get(self, incident_id):
        """method for getting a specific incident"""
        incident = self.db.find_by_id(incident_id)
        if incident == "incident does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "incident does not exit"
            }), 404)

        return make_response(jsonify({
            "status": 200,
            "data": incident
        }), 200)

    def delete(self, incident_id):
        """docstring for deleting an incident"""
        incident = self.db.find_by_id(incident_id)
        if incident is "incident does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "rincident does not exit"
            }), 404)
        delete_status = self.db.delete(incident_id)
        if delete_status == "deleted":
            return make_response(jsonify({
                "status": 200,
                "data": 'incident record has been deleted'
            }), 200)


class UpdateLocation(Resource):
    """class to update incident location"""

    def __init__(self):
        """initiliase the update location class"""
        self.db = IncidentModel()

    def patch(self, incident_id):
        """method to update redflag location"""
        incident = self.db.find_by_id(incident_id)

        if incident == "incident does not exist":
            return make_response(jsonify({
                "status": 404,
                "error": "Incident does not exist"
            }), 404)
        edit_status = self.db.edit_incident_location(incident_id)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError Incidents location not updated"
            }), 500)
        elif edit_status == "location updated":
            return make_response(jsonify({
                "status": 200,
                "data": {
                    "id": incident_id,
                    "message": "Updated incident record's location"
                }
            }), 200)


class UpdateComment(Resource):
    """docstring for patching comment"""

    def __init__(self):
        self.db = IncidentModel()

    def patch(self, incident_id):
        """method to update comment in an incident"""
        incident = self.db.find_by_id(incident_id)

        if incident == "incident does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "incident does not exit"
            }), 404)

        edit_status = self.db.edit_incident_comment(incident_id)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError Incident's comment not updated"
            }), 500)
        elif edit_status == "comment updated":
            return make_response(jsonify({
                "status": 200,
                "data": {
                    "id": incident_id,
                    "message": "Updated incident record's comment"
                }
            }), 200)

class UpdateStatus(Resource):
    """docstring for patching status"""

    def __init__(self):
        self.db = IncidentModel()

    def patch(self, incident_id):
        """method to update status in an incident"""
        incident = self.db.find_by_id(incident_id)

        if incident == "incident does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "incident does not exit"
            }), 404)

        edit_status = self.db.edit_incident_status(incident_id)
        if edit_status == "keyerror":
            return make_response(jsonify({
                "status": 500,
                "error": "KeyError Incident's comment not updated"
            }), 500)
        elif edit_status == "status updated":
            return make_response(jsonify({
                "status": 200,
                "data": {
                    "id": incident_id,
                    "message": "Updated incident's status"
                }
            }), 200) 

class Filter(Resource):
    """docstring filtering incidents by type"""

    def __init__(self):
        """initiliase the incident class"""
        self.db = IncidentModel()

    def get(self, incident_type):
        """method for getting a specific group of incidents"""
        incident = self.db.find_by_type(incident_type)
        if incident == "incident does not exit":
            return make_response(jsonify({
                "status": 404,
                "error": "incident does not exit"
            }), 404)

        return make_response(jsonify({
            "status": 200,
            "data": incident
        }), 200)
