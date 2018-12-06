"""Tests for redflags run with pytest"""
import json
import unittest

from ... import create_app


class RedFlagTestCase(unittest.TestCase):
    """
    This class represents the redflag test cases
    """

    def setUp(self):
        APP = create_app("testing")
        self.app = APP.test_client()

        self.redflag = {
            "createdBy": 5,
            "type": "red-flag",
            "location": "66, 12",
            "status": "resolved",
            "images": "",
            "videos": "",
            "title": "NYS scandal",
            "comment": "53"

        }

    def test_get_all_redflags(self):
        """method to test get all"""
        response = self.app.get("/api/v1/red-flags")
        self.assertEqual(response.status_code, 200)

    def test_post_redflag(self):
        response = self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.redflag))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Created red-flag record', str(result))

    def test_get_specific_redflag(self):
        """method to test if one can get a specific redflag"""
        self.app.post("/api/v1/red-flags",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.redflag))
        response = self.app.get("/api/v1/red-flags/1")
        json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_delete_specific_redflag(self):
        """method to test if one can delete a redflag"""
        self.app.post("/api/v1/red-flags",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.redflag))
        response = self.app.delete("/api/v1/red-flags/1")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('red-flag record has been deleted', str(result))

    def test_update_location_of_specific_redflag(self):
        """method to test edit of location"""
        self.app.post("/api/v1/red-flags/1/location",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.redflag))
        response = self.app.patch("/api/v1/red-flags/1/location", headers={
                                  'Content-Type': 'application/json'}, data=json.dumps({"location": "24.0 , 12.0"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Updated red-flag record's location", str(result))

    def test_update_comment_of_specific_redflag(self):
        """method to test edit of comment"""
        self.app.post("/api/v1/red-flags/1/comment",
                      headers={'Content-Type': 'application/json'}, data=json.dumps(self.redflag))
        response = self.app.patch("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'},
                                  data=json.dumps({"comment": "hello cohart 35"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated red-flag record's comment",
                      str(result))

    def test_redflag_not_found(self):
        """Test a redflag not found"""
        response = self.app.get("/api/v1/red-flags/100")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(
            result['error'], "red flag does not exit")

    def test_wrong_comment_key(self):
        """Test wrong comment key used in redflag"""
        response = self.app.patch("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'},
                                  data=json.dumps({"comment1": "hello pac"}))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 500)
        self.assertEqual(
            result['error'], "KeyError Red-flag's comment not updated")
