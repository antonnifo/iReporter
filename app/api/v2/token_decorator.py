import datetime
import os
from functools import wraps

import jwt
from flask import jsonify, make_response, request

from app.api.v2.users.models import UserModel

# secret = os.getenv('SECRET_KEY')
secret = "Bssc010j2014"

def require_token(f):
    @wraps(f)
    def secure(*args, ** kwargs):
        token = None

        if 'token' in request.headers:
            token = request.headers['token']
        if not token:
            return make_response(jsonify({
                "message": "Token is missing"
            }), 401)

        try:
            data = jwt.decode(token, secret)
            current_user = UserModel().find_user_by_email(data['email'])

        except:
            return make_response(jsonify({
                "message": "Token is invalid"
            }), 401)
        return f(current_user, *args, **kwargs)
    return secure
