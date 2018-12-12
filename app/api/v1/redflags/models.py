"""model for view for incidents"""
import datetime

from flask import jsonify, make_response, request
from flask_restful import Resource, reqparse
from .validators import validator_integer, validate_coordinates, validate_string

parser = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('createdBy',
                    type=validator_integer,
                    required=True,
                    help="Value Must be an Interger as it is an ID or cant be left blank"
                    )

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
parser.add_argument('status',
                    type=str,
                    required=True,
                    choices=("resolved", "under investigation", "rejected"),
                    help="This field cannot be left blank or should only be resolved ,under investigation or rejected"
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

incidents = []


class RedFlagModel():
    """Class with methods to perform CRUD operations on the DB"""
    def __init__(self):
        self.db = incidents
        if len(incidents) == 0:
            self.id = 1
        else:
            self.id = incidents[-1]['id'] + 1
        self.id = len(incidents) + 1

    def save(self):
        parser.parse_args()
        data = {
            'id': self.id,
            'createdOn': datetime.datetime.utcnow(),
            'createdBy': request.json.get('createdBy'),
            'type': 'red-flags',
            'location': request.json.get('location'),
            'status': "under investigation",
            'images': request.json.get('images'),
            'videos': request.json.get('videos'),
            'title': request.json.get('title'),
            'comment': request.json.get('comment')
        }
        
        self.db.append(data)
        return self.id

    def find(self, redflag_id):
        for incident in self.db:
            if incident['id'] == redflag_id:
                return incident

        return "red flag does not exit"

    def delete(self, incident):
        self.db.remove(incident)
        return "deleted"

    def get_all(self):
        return self.db

    def edit_redflag_location(self, incident):
        "Method to edit a redflag's location"
        incident['location'] = request.json.get('location', 'keyerror')
        if incident['location'] == 'keyerror':
            return "keyerror"
        return "updated"

    def edit_redflag_comment(self, incident):
        "Method to edit a redflag's comment"
        incident['comment'] = request.json.get('comment', 'keyerror')
        if incident['comment'] == 'keyerror':
            return "keyerror"
        return "updated"

    def edit_redflag(self, incident):
        """Method to edit redflag fields"""
        parser.parse_args()
        incident['createdBy'] = request.json.get(
            'createdBy', incident['createdBy'])
        incident['location'] = request.json.get(
            'location', incident['location'])
        incident['status'] = request.json.get('status', incident['status'])
        incident['images'] = request.json.get('images', incident['images'])
        incident['videos'] = request.json.get('videos', incident['videos'])
        incident['title'] = request.json.get('title', incident['title'])
        incident['comment'] = request.json.get('comment', incident['comment'])

        return "updated"
