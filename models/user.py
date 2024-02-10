#!/usr/bin/python3
"""
Module for the User class which inherits from BaseModel.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.

    Attributes:
        email (str): Empty string.
        password (str): Empty string.
        first_name (str): Empty string.
        last_name (str): Empty string.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
