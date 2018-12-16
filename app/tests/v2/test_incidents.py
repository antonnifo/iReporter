"""Tests for incidents in v2 run with pytest"""
import datetime
import json
import os
import unittest

import jwt

from ... import create_app
from app.db_con import create_tables, test_user_admin, test_intervention, test_redflag, destroy_tables

secret = os.getenv('SECRET_KEY')


class IncidentTestCase(unittest.TestCase):
    """
    This class represents the incident test cases
    """

    def setUp(self):
        APP = create_app("testing")
        self.app = APP.test_client()
        create_tables()
        test_user_admin()
        test_intervention()
        test_redflag()
        self.test_user = {
            "first_name": "john",
            "last_name": "doe",
            "email": "johndoe@example.com",
            "phone": "0708767676",
            "isAdmin": True,
            "date_created": "Thu, 13 Dec 2018 21:00:00 GMT",
            "password": "pbkdf2:sha256:50000$OwVe1ERR$ccdcf27b466c87f3fdf581183693536651e0dd8094c68d281b224375addcba3d"
        }
        payload = {
            "email": self.test_user['email'],
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(
            payload=payload, key="Bssc010j2014", algorithm='HS256')
        self.headers = {'Content-Type': 'application/json',
                        'token': token
                        }

        self.headers_invalid = {
            'Content-Type': 'application/json', 'token': 'Tokenmbaya'}

        self.intervention = {
            "createdBy": 1,
            "type": "intervention",
            "location": "66, 12",
            "status": "draft",
            "title": "NYS scandal",
            "comment": "act soon",
            "createdon": "Thu, 13 Dec 2018 14:31:20 GMT"
        }

        self.redflag = {
            "createdBy": 1,
            "type": "redflag",
            "location": "66, 12",
            "status": "draft",
            "title": "NYS scandal",
            "comment": "act soon",
            "createdon": "Thu, 13 Dec 2018 14:31:20 GMT"

        }

    def test_get_all_interventions_no_token(self):
        """method to test get all incidents with no token"""
        response = self.app.get("/api/v2/interventions")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(result['message'], "Token is missing")

    def test_get_all_redflags_no_token(self):
        """method to test get all incidents with no token"""
        response = self.app.get("/api/v2/redflags")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(result['message'], "Token is missing")

    def test_get_all_intervention_invalid_token(self):
        """method to test get all incidents with invalid  token"""
        response = self.app.get(
            "/api/v2/interventions", headers=self.headers_invalid)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(result['message'], "Token is invalid")

    def test_get_all_redflag_invalid_token(self):
        """method to test get all incidents with invalid  token"""
        response = self.app.get(
            "/api/v2/redflags", headers=self.headers_invalid)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(result['message'], "Token is invalid")

    def test_delete_intervention_withiout_ownership(self):
        """method to test if one can delete an incident"""
        self.app.post("/api/v2/interventions",
                      headers=self.headers, data=json.dumps(self.intervention))
        response = self.app.delete("/api/v2/intervention/1")
        json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_redflag_withiout_ownership(self):
        """method to test if one can delete an incident"""
        self.app.post("/api/v2/interventions",
                      headers=self.headers, data=json.dumps(self.redflag))
        response = self.app.delete("/api/v2/redflag/2")
        json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_intervention_withiout_token(self):
        """method to test if one can delete an incident"""
        self.app.post("/api/v2/interventions",
                      data=json.dumps(self.intervention))
        response = self.app.delete("/api/v2/intervention/1")
        json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_redflag_withiout_token(self):
        """method to test if one can delete an incident"""
        self.app.post("/api/v2/interventions",
                      data=json.dumps(self.redflag))
        response = self.app.delete("/api/v2/redflag/2")
        json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_intervention_with_invalid_token(self):
        """method to test if one can delete an incident"""
        self.app.post("/api/v2/interventions",
                      headers=self.headers_invalid, data=json.dumps(self.intervention))
        response = self.app.delete("/api/v2/intervention/1")
        json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_delete_redflag_with_invalid_token(self):
        """method to test if one can delete an incident"""
        self.app.post("/api/v2/interventions",
                      headers=self.headers_invalid, data=json.dumps(self.redflag))
        response = self.app.delete("/api/v2/redflag/2")
        json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def tearDown(self):
        destroy_tables()
