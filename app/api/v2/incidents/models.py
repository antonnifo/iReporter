"""Incidents Models"""
import datetime
from flask import request
from flask_restful import reqparse
from app.db_con import connection, url, cursor
import re
import psycopg2.extras
from .validators import validate_integer, validate_coordinates, validate_string

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('location',
                    type=validate_coordinates,
                    required=True,
                    help="This field cannot be left blank or improperly formated"
                    )

parser.add_argument('type',
                    type=str,
                    required=True,
                    choices=("red-flag", "intervention"),
                    help="This field cannot be left "
                         "blank or Bad choice: {error_msg}"
                    )

parser.add_argument('images',
                    action='append',
                    help="This field can be left blank!"
                    )
parser.add_argument('videos',
                    action='append',
                    help="This field can be left blank!"
                    )

parser.add_argument('comment',
                    type=validate_string,
                    required=True,
                    help="This field cannot be left blank or should be properly formated"
                    )
parser.add_argument('title',
                    type=validate_string,
                    required=True,
                    help="This field cannot be left blank or should be properly formated"
                    )


class IncidentModel:
    """Class with methods to perform CRUD operations on the DB"""

    def __init__(self):
        self.db = connection(url)
        self.cursor = cursor(url)

    def save(self, user_id):
        parser.parse_args()
        data = {
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': user_id,
            'type': request.json.get('type'),
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

    def find_by_type(self, incident_type):
        query = """SELECT * from incidents WHERE type='{0}'""".format(
            incident_type)
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)    
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def find_by_id(self, incident_id):
        query = """SELECT * from incidents WHERE  incidents_id={0}""".format(
        incident_id) 
        conn = self.db
        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)    
        cursor.execute(query)     
        result = cursor.fetchone()
        if cursor.rowcount == 0:
            return 'incident does not exit'
        return result

    def edit_incident_status(self, incident_id):
        "Method to edit an incident's status"
        status = request.json.get('status')
        if self.find_by_id(incident_id) == None:
            return None

        query = """UPDATE incidents SET status='{0}' WHERE incidents_id={1}""".format(
            status, incident_id)
        con = self.db
        self.cursor.execute(query)
        con.commit()
        return 'status updated'

    def find_all(self):
        """method to find all incidents"""
        query = """SELECT * from incidents"""
        con = self.db
        cursor = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        incidents =cursor.fetchall()
        return incidents

    def edit_incident_location(self, incident_id):
        "Method to edit an incident's location"
        location = request.json.get('location')
        incident = self.find_by_id(incident_id)
        if incident == "incident does not exit":
            return None

        query = """UPDATE incidents SET location='{0}' WHERE incidents_id={1}""".format(
            location, incident_id)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'location updated'

    def edit_incident_comment(self, incident_id):
        "Method to edit an incident's comment"
        comment = request.json.get('comment')
        incident = self.find_by_id(incident_id)
        if incident == "incident does not exit":
            return None
        query = """UPDATE incidents SET comment='{0}' WHERE incidents_id={1}""".format(
            comment, incident_id)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'comment updated'

    def delete(self, incident_id):
        "Method to delete an incident record by id"
        incident = self.find_by_id(incident_id)
        if incident is None:
            return None

        query = """DELETE FROM incidents WHERE incidents_id={0}""".format(
            incident_id)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'deleted'
