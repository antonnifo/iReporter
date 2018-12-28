"""Tests for validators run with pytest"""
import unittest
from app.api.v2.validators import (
    validate_coordinates, validate_email, validate_integer, validate_password, validate_string)


class ValidatorsTestCase(unittest.TestCase):

    def test_for_integers(self):
        with self.assertRaises(ValueError):
            validate_integer("843ant")

    def test_for_strings(self):
        with self.assertRaises(ValueError):
            validate_string("@##$$Hello")

    def test_for_email(self):
        with self.assertRaises(ValueError):
            validate_email("antonnifogmail.com")

    def test_for_coordinates(self):
        with self.assertRaises(ValueError):
            validate_coordinates("-421, 567")

    def test_for_password(self):
        with self.assertRaises(ValueError):
            validate_password(" ")
