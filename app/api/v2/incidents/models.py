"""Incidents Models"""
import datetime
from flask import request
from flask_restful import reqparse
from app.db_con import connection
from app.db_con import DATABASE_URL as url
import re
import psycopg2.extras
from ..validators import parser, parser_edit_location, parser_edit_comment, parser_edit_status


class IncidentModel:
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = connection(url)

    def save(self, user_id, incident_type):
        parser.parse_args()
        data = {
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': user_id,
            'type': incident_type,
            'location': request.json.get('location'),
            'status': "draft",
            'title': request.json.get('title'),
            'comment': request.json.get('comment')
        }

        query = """INSERT INTO incidents (createdon,createdby,type,location,status,title,comment) VALUES('{0}',{1},'{2}','{3}','{4}','{5}','{6}');""".format(
            data['createdOn'], data['createdBy'], data['type'], data['location'], data['status'], data['title'], data['comment'])
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return data

    def find_status(self, incident_id):
        """method to find status of an incident"""
        query = """SELECT status from incidents WHERE  incidents_id={0} """.format(
            incident_id)
        con = self.db
        cursor = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        status = cursor.fetchone()
        if cursor.rowcount == 0:
            return 'incident does not exit'
        return status

    def find_by_type(self, incident_type):
        query = """SELECT * from incidents WHERE type='{0}'""".format(
            incident_type)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def find_by_id_type(self, incident_id, incident_type):
        query = """SELECT * from incidents WHERE  incidents_id={0} AND type='{1}'""".format(
            incident_id, incident_type)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        result = cursor.fetchone()
        if cursor.rowcount == 0:
            return 'incident does not exit'
        return result

    def find_all(self):
        """method to find all incidents"""
        query = """SELECT * from incidents"""
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        incidents = cursor.fetchall()
        return incidents

    def edit_incident_status(self, incident_id, incident_type):
        "Method to edit an incident's status"
        parser_edit_status.parse_args()
        status = request.json.get('status')

        if self.find_by_id_type(incident_id, incident_type) == "incident does not exit":
            return None

        query = """UPDATE incidents SET status='{0}' WHERE incidents_id={1}""".format(
            status, incident_id)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'status updated'

    def edit_incident_location(self, current_user_id, incident_id, incident_type):
        "Method to edit an incident's location"
        parser_edit_location.parse_args()
        location = request.json.get('location')

        incident = self.find_by_id_type(incident_id, incident_type)

        if incident == "incident does not exit":
            return None

        if current_user_id != incident['createdby']:
            return False

        status = self.find_status(incident_id)
        if status != {'status': 'draft                                                           '}:
            return 'you cant edit this'

        query = """UPDATE incidents SET location='{0}' WHERE incidents_id={1}""".format(
            location, incident_id)

        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'location updated'

    def edit_incident_comment(self, incident_id, incident_type):
        "Method to edit an incident's comment"
        parser_edit_comment.parse_args()
        comment = request.json.get('comment')
        incident = self.find_by_id_type(incident_id, incident_type)

        if incident == "incident does not exit":
            return None

        status = self.find_status(incident_id)
        if status != {'status': 'draft                                                           '}:
            return 'you cant edit this'

        query = """UPDATE incidents SET comment='{0}' WHERE incidents_id={1}""".format(
            comment, incident_id)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'comment updated'

    def delete(self, incident_id, incident_type):
        "Method to delete an incident record by id"
        incident = self.find_by_id_type(incident_id, incident_type)
        if incident is None:
            return None

        query = """DELETE FROM incidents WHERE incidents_id={0}""".format(
            incident_id)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'deleted'
