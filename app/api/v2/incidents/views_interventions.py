"""Views for Interventions"""
from flask import jsonify, make_response, request
from flask_restful import Resource

from app.api.v2.users.models import UserModel

from ..validators import (can_only_edit_draft, non_existance_incident,
                          only_admin_can_edit, only_creater_can_delete,
                          only_creater_can_edit)
from .models import IncidentModel
from app.api.v2.token_decorator import require_token


class Interventions(Resource):
    """docstring for interventions class"""

    def __init__(self):
        """initiliase the interventions class"""
        self.db = IncidentModel()

    @require_token
    def post(current_user, self):
        """method for saving an intervention"""
        incident = self.db.save(
            current_user['user_id'], incident_type='intervention')
        return jsonify({
            "status": 201,
            "data": incident,
            "message": "Created intervention record"
        })

    @require_token
    def get(current_user, self):
        """method for getting all the interventions posted by users"""
        self.db.find_by_type(incident_type='intervention')
        return jsonify({
            "status": 200,
            "data": self.db.find_by_type(incident_type='intervention')
        })


class Intervention(Resource):
    """docstring of a single intervention"""

    def __init__(self):
        """initiliase the intervention class"""
        self.db = IncidentModel()

    @require_token
    def get(current_user, self, incident_id):
        """method for getting a specific intervention"""
        incident = self.db.find_by_id_type(
            incident_id, incident_type='intervention')
        if incident == "incident does not exit":
            return non_existance_incident()

        return jsonify({
            "status": 200,
            "data": incident
        })

    @require_token
    def delete(current_user, self, incident_id):
        """docstring for deleting an intervention"""
        incident = self.db.find_by_id_type(
            incident_id, incident_type='intervention')
        if incident == "incident does not exit":
            return non_existance_incident()

        if current_user["user_id"] != incident["createdby"]:
            return only_creater_can_delete()

        if self.db.delete(incident_id, incident_type='intervention') == "deleted":
            return jsonify({
                "status": 200,
                "message": 'incident record has been deleted'
            })


class UpdateInterventionLocation(Resource):
    """class to update intervention location"""

    def __init__(self):
        """initiliase the update location class of an intervention"""
        self.database = IncidentModel()

    @require_token
    def patch(current_user, self, incident_id):
        """method to update an intervention location"""

        edit_status = self.database.edit_incident_location(
            current_user['user_id'],incident_id, incident_type='intervention')
        
        if edit_status is None:
            return non_existance_incident()

        if edit_status is False:
            return only_creater_can_edit()

        if edit_status == 'you cant edit this':
            return can_only_edit_draft()

        if edit_status == "location updated":
            return jsonify({
                "status": 200,
                "data": {
                    "id": incident_id,
                    "message": "Updated intervention record's location"
                }
            })


class UpdateInterventionComment(Resource):
    """docstring for patching an intervention comment"""

    def __init__(self):
        self.db = IncidentModel()

    @require_token
    def patch(current_user, self, incident_id):
        """method to update comment of an intervention"""
        incident = self.db.find_by_id_type(
            incident_id, incident_type='intervention')
        if incident == "incident does not exit":
            return non_existance_incident()

        if current_user["user_id"] != incident['createdby']:
            return only_creater_can_edit()

        edit_status = self.db.edit_incident_comment(
            incident_id, incident_type='intervention')

        if edit_status == "you cant edit this":
            return can_only_edit_draft()

        if edit_status == "comment updated":
            return jsonify({
                "status": 200,
                "data": {
                    "id": incident_id,
                    "message": "Updated incident record's comment"
                }
            })


class UpdateInterventionStatus(Resource):
    """docstring for patching status of an intervention"""

    def __init__(self):
        self.db = IncidentModel()

    @require_token
    def patch(current_user, self, incident_id):
        """method to update status of an intervention"""
        if current_user['isadmin'] is False:
            return only_admin_can_edit()

        edit_status = self.db.edit_incident_status(
            incident_id, incident_type='intervention')

        if edit_status == None:
            return non_existance_incident()

        if edit_status == "status updated":
            return jsonify({
                "status": 200,
                "data": {
                    "id": incident_id,
                    "message": "Updated intervention's status"
                }
            })
