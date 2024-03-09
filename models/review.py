#!/usr/bin/python3
""" Module containing Review class. """

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits from BaseModel. """

    place_id = ""  # Public class attribute
    user_id = ""  # Public class attribute
    text = ""  # Public class attribute
