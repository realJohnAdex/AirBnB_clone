#!/usr/bin/python3
"""This module contains the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes User instance with specific attributes.
        """
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', "")
        self.password = kwargs.get('password', "")
        self.first_name = kwargs.get('first_name', "")
        self.last_name = kwargs.get('last_name', "")

    def __str__(self):
        """
        Returns string representation of User instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
