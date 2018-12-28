"""Tests for users run with pytest"""
import unittest
import json
import jwt
import datetime
import os

from ... import create_app
from app.db_con import create_tables, super_user, destroy_tables
from app.tests.v2.testing_data import (
    test_user, user, user2, user3, user4,data5, data6, data7)

secret = os.getenv('SECRET_KEY')


class UserTestCase(unittest.TestCase):
    """Class for User testcase"""

    def setUp(self):
        """set up method initialising resused variables"""
        APP = create_app(config_name="testing")
        APP.testing = True
        self.app = APP.test_client()
        create_tables()
        super_user()
        self.test_user = test_user
        payload = {
            "email": self.test_user['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }

        token = jwt.encode(
            payload=payload, key=secret, algorithm='HS256')

        self.headers = {'Content-Type': 'application/json',
                        'token': token
                        }

        self.data = user
        self.data2 = user2
        self.data3 = user3
        self.data4 = user4
        self.data5 = data5
        self.data6 = data6
        self.data7 = data7

    def test_user_signup(self):
        """Test user signup"""
        response = self.app.post(
            "/api/v2/auth/signup", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        print(response)
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_user_signin(self):
        """Test post a user signin"""
        self.app.post("/api/v2/auth/signup", headers={'Content-Type': 'application/json'},
                      data=json.dumps(self.data))
        response = self.app.post(
            "/api/v2/auth/signin", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data5))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_user_signin_wrong_password(self):
        """Test post a user signin"""
        self.app.post("/api/v2/auth/signup", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        response = self.app.post("/api/v2/auth/signin", headers=self.headers, data=json.dumps(self.data6))
        result = json.loads(response.data)
        print(result)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'], 'password or email is incorrect please try again')

    def test_duplicate_user_email(self):
        """Test signup a user with existing email"""
        self.app.post("/api/v2/auth/signup", headers={'Content-Type': 'application/json'},
                      data=json.dumps(self.data))
        response = self.app.post(
            "/api/v2/auth/signup", headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        result = json.loads(response.data)
        self.assertEqual(result['status'], 400)
        self.assertEqual(result['error'], "email already exists")

    def test_get_users(self):
        """Test to get all users"""
        response = self.app.get(
            "/api/v2/users", headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_get_specific_user(self):
        """Test get a specific redflag"""
        self.app.post("/api/v2/auth/signup",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.data))
        response = self.app.get(
            "/api/v2/users/john@doe.com", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_nonexistent_user(self):
        """Test to check a user who does not exist"""
        response = self.app.get("/api/v2/users/kama@gmail.com", headers=self.headers)
        self.assertEqual(response.status_code, 200)
        result = json.loads(response.data)
        self.assertEqual(result['message'], 'user does not exist')

    def test_delete_specific_user(self):
        """Test delete a specific redflag"""
        self.app.post("/api/v2/auth/signup", headers=self.headers, data=json.dumps(self.data))
        response = self.app.delete("/api/v2/users/john@doe.com", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_update_user_status(self):
        """Test to update user admin status"""
        self.app.post("/api/v2/auth/signup", headers=self.headers, data=json.dumps(self.data))
        response = self.app.patch("/api/v2/users/john@doe.com/status", headers=self.headers, data=json.dumps({"isadmin":"False"}))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        destroy_tables() 