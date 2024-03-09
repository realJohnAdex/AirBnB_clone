#!/usr/bin/python3
""" Module containing City class. """

from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel. """

    state_id = ""  # Public class attribute
    name = ""  # Public class attribute
