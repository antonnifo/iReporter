"""for fields validations"""
import re
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
    """method to check comment only contains letters"""
    if not re.match(r"[A-Za-z1-9]+", value):
        raise ValueError("Pattern not matched")


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
