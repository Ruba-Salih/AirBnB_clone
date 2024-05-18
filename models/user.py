#!/usr/bin/python3
"""
User class definition
"""
from models import BaseModel

class User(BaseModel):
    """
    User class
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """