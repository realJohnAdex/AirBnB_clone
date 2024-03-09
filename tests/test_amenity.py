#!/usr/bin/python3
""" Module containing tests for Amenity class. """

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Class containing tests for the Amenity class. """

    def test_instantiation(self):
        """ Test that instance of Amenity class is created. """
        a = Amenity()
        self.assertIsInstance(a, BaseModel)
        self.assertIsInstance(a, Amenity)

    def test_attributes(self):
        """ Test that Amenity class has the required attributes. """
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")
        self.assertEqual(a.__class__.__name__, "Amenity")

    def test_str(self):
        """ Test that the str method has the correct output. """
        a = Amenity()
        string = "[Amenity] ({}) {}".format(a.id, a.__dict__)
        self.assertEqual(string, str(a))

    def test_inheritance(self):
        """ Test that Amenity class inherits from BaseModel. """
        a = Amenity()
        self.assertTrue(issubclass(type(a), BaseModel))
