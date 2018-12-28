"""Tests for incidents in v2 run with pytest"""
import datetime
import json
import os
import unittest

import jwt

from ... import create_app
from app.db_con import create_tables, super_user, destroy_tables
from app.tests.v2.testing_data import (
    test_user, user, user2, user3, user4, redflag_data, redflag_data3, redflag_data2, data5, data6, data7, intervention_data)

secret = os.getenv('SECRET_KEY')

class IncidentTestCase(unittest.TestCase):
    """
    This class represents the incident test cases
    """

    def setUp(self):
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

        assert "exp" in payload

        token = jwt.encode(
            payload=payload, key=secret, algorithm='HS256')

        self.headers = {'Content-Type': 'application/json',
                        'token': token
                        }

        self.headers_invalid = {
            'Content-Type': 'application/json', 'token': 'Tokenmbaya'}

        self.intervention = intervention_data
        self.redflag = redflag_data
        self.redflag_data2 = redflag_data2
        self.redflag_data3 = redflag_data3
    
    def test_get_all_redflags(self):
        """Test all redflags"""
        response = self.app.get("/api/v2/redflags", headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_all_interventions(self):
        """Test all redflags"""
        response = self.app.get("/api/v2/interventions", headers=self.headers)
        self.assertEqual(response.status_code, 200)

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
    
    def test_get_specific_redflag(self):
        """Test get a specific redflag"""
        self.app.post("/api/v2/redflags", headers=self.headers,
                      data=json.dumps(self.redflag))
        response = self.app.get("/api/v2/redflag/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
    
    def test_get_specific_intervention(self):
        """Test get a specific intervention"""
        self.app.post("/api/v2/interventions", headers=self.headers,
                      data=json.dumps(self.redflag))
        response = self.app.get(
            "/api/v2/intervention/1", headers=self.headers)
        self.assertEqual(response.status_code, 200)
    
    def test_post_redflag(self):
        """Test post a redflag"""
        response = self.app.post(
            "/api/v2/redflags", headers=self.headers, data=json.dumps(self.redflag))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 201)
    
    def test_post_intervention(self):
        """Test post a intervention"""
        response = self.app.post(
            "/api/v2/interventions", headers=self.headers, data=json.dumps(self.redflag))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['status'], 201)
    
    def test_update_status_of_nonexistent_redflag(self):
        """Test update status of a nonexistant redflag"""       
        response = self.app.patch(
            "/api/v2/redflags/2/status", headers=self.headers, data=json.dumps({"status": "resolved"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], 'incident does not exist')

    def test_update_status_of_redflag(self):
        """Test update status of a specific redflag"""
        self.app.post(
            "/api/v2/redflags", headers=self.headers, data=json.dumps(self.redflag))        
        response = self.app.patch(
            "/api/v2/redflags/1/status", headers=self.headers, data=json.dumps({"status": "resolved"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_update_location_of_nonexistent_redflag(self):
        """Test update location of a specific redflag"""       
        response = self.app.patch(
            "/api/v2/redflags/2/location", headers=self.headers, data=json.dumps({"location": "-75.0, -12.554334"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], 'incident does not exist') 
    
    def test_update_location_of_redflag(self):
        """Test update location of a specific redflag"""
        self.app.post(
            "/api/v2/redflags", headers=self.headers, data=json.dumps(self.redflag))        
        response = self.app.patch("/api/v2/redflags/1/location", headers=self.headers,
                                  data=json.dumps({"location": "-75.0, -12.554334"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_comment_of_nonexistent_redflag(self):
        """Test update comment of a specific redflag"""       
        response = self.app.patch(
            "/api/v2/redflags/2/comment", headers=self.headers, data=json.dumps({"comment": "You Only Live Once"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], 'incident does not exist') 
    
    def test_update_comment_of_redflag(self):
        """Test update comment of a specific redflag"""
        self.app.post(
            "/api/v2/redflags", headers=self.headers, data=json.dumps(self.redflag))        
        response = self.app.patch("/api/v2/redflags/1/comment", headers=self.headers,
                                  data=json.dumps({"comment": "You Only Live Once"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_update_location_of_intervention(self):
        """Test update location of a specific intervention"""
        self.app.post(
            "/api/v2/interventions", headers=self.headers, data=json.dumps(self.redflag))         
        response = self.app.patch("/api/v2/interventions/1/location",
                                  headers=self.headers, data=json.dumps({"location": "-75.0, -12.554334"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)
      

    def test_update_comment_of_nonexistent_intervention(self):
        """Test update comment of a specific intervention"""       
        response = self.app.patch(
            "/api/v2/interventions/254534423/comment", headers=self.headers, data=json.dumps({"comment": "You only live once"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], 'incident does not exist') 

    def test_update_comment_of_intervention(self):
        """Test update comment of a specific intervention"""
        self.app.post(
            "/api/v2/interventions", headers=self.headers, data=json.dumps(self.redflag))         
        response = self.app.patch("/api/v2/interventions/1/comment", headers=self.headers,
                                  data=json.dumps({"comment": "Cartels are taking over Kenya"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

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

    def test_update_status_of_nonexistent_intervention(self):
        """Test update status of a nonexistant intervention"""       
        response = self.app.patch(
            "/api/v2/interventions/266855866/status", headers=self.headers, data=json.dumps({"status": "resolved"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], 'incident does not exist')         

    def test_update_status_of_intervention(self):
        """Test update status of a specific intervention"""
        self.app.post(
            "/api/v2/interventions", headers=self.headers, data=json.dumps(self.redflag))        
        response = self.app.patch("/api/v2/interventions/1/status",
                                  headers=self.headers, data=json.dumps({"status": "resolved"}))
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        
    def test_wrong_status_key_redflag(self):
        """Test wrong status key used in redflag"""
        response = self.app.patch(
            "/api/v2/redflags/1/status", headers=self.headers, data=json.dumps({"status1": "draft  "}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['status'],
                         "This field cannot be left blank or should only be resolved ,under investigation or rejected")

    def test_wrong_status_choice_in_redflag(self):
        """Test wrong status key used in redflag"""
        response = self.app.patch(
            "/api/v2/redflags/1/status", headers=self.headers, data=json.dumps({"status": "drafted"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['status'],
                         "This field cannot be left blank or should only be resolved ,under investigation or rejected")

    def test_wrong_location_key_redflag(self):
        """Test wrong location key used in redflag"""
        response = self.app.patch("/api/v2/redflags/1/location",
                                  headers=self.headers, data=json.dumps({"location1": "Mombao"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['location'],
                         "This field cannot be left blank or improperly formated")

    def test_wrong_status_key_intervention(self):
        """Test wrong status key used in intervention"""
        response = self.app.patch("/api/v2/interventions/1/status",
                                  headers=self.headers, data=json.dumps({"status1": "draft"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['status'],
                         "This field cannot be left blank or should only be resolved ,under investigation or rejected")

    def test_wrong_status_choice_in_intervention(self):
        """Test wrong status key used in intervention"""
        response = self.app.patch("/api/v2/interventions/1/status",
                                  headers=self.headers, data=json.dumps({"status": "drafted"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['status'],
                         "This field cannot be left blank or should only be resolved ,under investigation or rejected")

    def test_wrong_location_key_intervention(self):
        """Test wrong location key used in intervention"""
        response = self.app.patch("/api/v2/interventions/1/location",
                                  headers=self.headers, data=json.dumps({"location1": "Nairobi"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(result['message']['location'],
                         "This field cannot be left blank or improperly formated")

    def test_redflag_not_found(self):
        """Test a redflag not found"""
        response = self.app.get("/api/v2/redflag/10000", headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], "incident does not exist")

    def test_intervention_not_found(self):
        """Test a redflag not found"""
        response = self.app.get(
            "/api/v2/intervention/10000", headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['error'], "incident does not exist")

    def test_missing_key_redflag(self):
        """Test missing key in redflag"""
        response = self.app.post(
            "/api/v2/redflags", headers=self.headers, data=json.dumps(self.redflag_data3))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)

    def test_missing_key_intervention(self):
        """Test missing key in intervention"""
        response = self.app.post(
            "/api/v2/interventions", headers=self.headers, data=json.dumps(self.redflag_data3))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 400)

    def test_delete_specific_redflag(self):
        """Test delete a specific redflag"""
        self.app.post("/api/v2/redflags", headers=self.headers,
                      data=json.dumps(self.redflag))
        response = self.app.delete("/api/v2/redflag/1", headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'],
                         'incident record has been deleted')

    def test_delete_specific_intervention(self):
        """Test delete a specific intervention"""
        self.app.post("/api/v2/interventions", headers=self.headers,
                      data=json.dumps(self.redflag))
        response = self.app.delete(
            "/api/v2/intervention/1", headers=self.headers)
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(result['message'],
                         'incident record has been deleted')

    def tearDown(self):
        destroy_tables()
