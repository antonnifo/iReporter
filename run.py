"""Run docstring"""

import os
from flask import jsonify, make_response

from app import create_app

APP = create_app(os.getenv("FLASK_CONF") or 'default')

@APP.errorhandler(404)
def page_not_found(e):
    """error handler default method for error 404"""

    return make_response(
        jsonify(
            {"message": "Oops! not found, check you have "
             "right url or correct input type", "status": 404}
            ), 404
        )
