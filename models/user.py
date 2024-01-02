#!/usr/bin/python3
"""
user module - defines the User class for account
creation 
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class defines methods for user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
