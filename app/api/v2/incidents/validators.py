"""for validating imports"""
import re


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
    if not re.match(r"[A-Za-z1-9]", value):
        raise ValueError("Pattern not matched")
