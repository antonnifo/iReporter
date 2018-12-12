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
        """docstring for getting all the incidents posted"""
        self.db.find_all()
        return make_response(jsonify({
            "status": 200,
            "data": self.db.find_all()
        }), 200)
