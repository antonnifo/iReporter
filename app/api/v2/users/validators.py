"""for validating user details"""
import re


def validator_integer(value):
    """method to check for only integers"""
    if not re.match(r"^[0-9]+$", value):
        raise ValueError("Only Numbers are required")
    
def validate_string(value):
    """method to check comment only contains letters"""
    if not re.match(r"[A-Za-z1-9]", value):
        raise ValueError("letters and numbers only required")

def validate_email(value):
    """method to check for valid email"""
    if not re.match(r"^[^@]+@[^@]+\.[^@]+$", value):
        raise ValueError("write a proper Email")