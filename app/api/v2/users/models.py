'''model for users view file'''

import datetime

import psycopg2.extras
from flask import request
from flask_restful import reqparse
from werkzeug.security import check_password_hash, generate_password_hash

from app.db_con import connection, url
from .validators import validate_email, validate_string, validator_integer

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('first_name',
                    type=validate_string,
                    required=False,
                    nullable=False,
                    help="This field cannot be left blank or should be properly formated"
                    )

parser.add_argument('last_name',
                    type=validate_string,
                    required=False,
                    nullable=False,
                    help="This field cannot be left blank or should be properly formated"
                    )

parser.add_argument('email',
                    type=validate_email,
                    required=False,
                    nullable=True,
                    help="This field cannot be left blank or should be properly formated"
                    )

parser.add_argument('phone',
                    type=validator_integer,
                    required=False,
                    nullable=True,
                    help="This field cannot be left blank or should be properly formated"
                    )

parser.add_argument('password',
                    required=True,
                    nullable=False,
                    help="This field cannot be left blank or should be properly formated"
                    )


def cursor(url):
    con = connection(url)
    cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return cursor


class UserModel:
    """class for dealing with user data"""

    def __init__(self):
        self.registered = datetime.datetime.utcnow()
        self.isAdmin = False
        self.db = connection(url)
        self.cursor = cursor(url)

    def set_pswd(self, password):
        '''salting the passwords '''
        return generate_password_hash(password)

    def check_pswd(self, password):
        return check_password_hash(self.pwdhash, password)

    def save(self):
        parser.parse_args()
        data = {
            'first_name': request.json.get('first_name'),
            'last_name': request.json.get('last_name'),
            'email': request.json.get('email'),
            'phone': request.json.get('phone'),
            'password': self.set_pswd(request.json.get('password')),
            'isAdmin': self.isAdmin
        }

        user_by_email = self.find_user_by_email(data['email'])

        if user_by_email != None:
            return 'email already exists'
        query = """INSERT INTO users (first_name,last_name,email,phone,password,isAdmin) VALUES('{0}','{1}','{2}','{3}','{4}','{5}');""".format(
            data['first_name'], data['last_name'], data['email'], data['phone'], data['password'], data['isAdmin'])
        con = self.db
        cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(query)
        con.commit()
        return data

    def find_user_by_user_id(self, user_id=2):
        "Method to find a user by user_id"
        query = """SELECT * from users WHERE user_id='{0}'""".format(user_id)
        con = self.db
        cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute(query)
        row = self.cursor.fetchone()

        if self.cursor.rowcount == 0:
            return None
        return row

    def find_user_by_email(self, email):
        "Method to find a user by email"
        query = """SELECT * from users WHERE email='{0}'""".format(email)
        con = self.db
        cursor = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        row = cursor.fetchall()

        if cursor.rowcount == 0:
            return None
        return row

    def log_in(self):
        data = {
            'email': request.json.get('email'),
            'password': request.json.get('password')
        }
        user = self.find_user_by_email(data['email'])
        if user == None:
            return None
        if check_password_hash(user[0]['password'], data['password']) == False:
            return 'incorrect password'
        return user[0]['email']

    def find_users(self):
        """method to find all users"""
        query = """SELECT * from users"""
        con = self.db
        cursor = con.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

    def edit_user_status(self, email):
        """method to update a user to an admin user"""
        isAdmin = request.json.get('isadmin')
        query = """UPDATE users SET isadmin='{0}' WHERE email={1}""".format(
            isAdmin, email)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'promoted'

    def delete_user(self, email):
        """method to delete a user record"""
        query = """DELETE FROM users WHERE email={0}""".format(email)
        con = self.db
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        return 'deleted'
