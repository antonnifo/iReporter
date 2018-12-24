"""for fields validations purposes"""
import re

from flask import jsonify, request
from flask_restful import reqparse


def validate_integer(value):
    """method to check for only integers"""
    if not re.match(r"^[0-9]+$", value):
        raise ValueError("Pattern not matched")


def validate_coordinates(value):
    """method to check for valid coordinates"""
    if not re.match(r"^[-+]?([1-8]?\d(\.\d+)?|90(\.0+)?),\s*[-+]?(180(\.0+)?|((1[0-7]\d)|([1-9]?\d))(\.\d+)?)$", value):
        raise ValueError("Pattern not matched")


def validate_string(value):
    """method to check that the field takes only letters"""
    if not re.match(r"[A-Za-z1-9]+", value):
        raise ValueError("Pattern not matched")


def validate_password(value):
    """method to check if password contains more than 8 characters"""
    if not re.match(r"^[A-Za-z0-9!@#$%^&+*=]{8,}$", value):
        raise ValueError("Password should be at least 8 characters")


def validate_email(value):
    """method to check for valid email"""
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", value):
        raise ValueError("write a proper Email")


parser = reqparse.RequestParser(bundle_errors=True)
parser_edit_location = reqparse.RequestParser(bundle_errors=True)
parser_edit_comment = reqparse.RequestParser(bundle_errors=True)
parser_edit_status = reqparse.RequestParser(bundle_errors=True)

parser.add_argument('location',
                    type=validate_coordinates,
                    required=True,
                    help="This field cannot be left blank or improperly formated"
                    )
parser_edit_location.add_argument('location',
                                  type=validate_coordinates,
                                  required=True,
                                  help="This field cannot be left blank or improperly formated"
                                  )
parser.add_argument('comment',
                    type=validate_string,
                    required=True,
                    help="This field cannot be left blank or should be properly formated"
                    )
parser_edit_comment.add_argument('comment',
                                 type=validate_string,
                                 required=True,
                                 help="This field cannot be left blank or should be properly formated"
                                 )
parser_edit_status.add_argument('status',
                                type=str,
                                required=True,
                                choices=(
                                    "resolved", "under investigation", "rejected"),
                                help="This field cannot be left blank or should only be resolved ,under investigation or rejected"
                                )
parser.add_argument('title',
                    type=validate_string,
                    required=True,
                    help="This field cannot be left blank or should be properly formated"
                    )


def non_existance_incident():
    '''return message for an incident that does not exist'''
    return jsonify({
        "status": 404,
        "error": "incident does not exit"
    })


def only_creater_can_edit():
    '''return message for only creater of an incident can patch it'''
    jsonify({
            "status": 401,
            "error": "sorry you can't edit an incident you din't create"
            })


def only_admin_can_edit():
    '''return message for only an admin can change status of an incident'''
    jsonify({
            "status": 403,
            "message": "sorry Only an admin can change the status of an incident"
            })


def only_creater_can_delete():
    '''return message that only create of an incident can delete it'''
    jsonify({
            "status": 401,
            "error": "sorry you can't delete an incident you din't create"
            })


def can_only_edit_draft():
    '''return message that u can patch an incident only on its draft state'''
    jsonify({
            "status": 401,
            "error": "You can't edit this due to it's state"
            })
