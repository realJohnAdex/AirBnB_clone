#!/usr/bin/python3
""" Module containing Place class. """

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class that inherits from BaseModel. """

    city_id = ""  # Public class attribute
    user_id = ""  # Public class attribute
    name = ""  # Public class attribute
    description = ""  # Public class attribute
    number_rooms = 0  # Public class attribute
    number_bathrooms = 0  # Public class attribute
    max_guest = 0  # Public class attribute
    price_by_night = 0  # Public class attribute
    latitude = 0.0  # Public class attribute
    longitude = 0.0  # Public class attribute
    amenity_ids = []  # Public class attribute
