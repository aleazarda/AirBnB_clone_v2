#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = 'gui@hbtn.io'
    password = 'guipwd'
    first_name = 'Guillaume'
    last_name = 'Snow'
