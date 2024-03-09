#!/usr/bin/python3
""" Module containing tests for City class. """

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """ Class containing tests for the City class. """

    def test_instantiation(self):
        """ Test that instance of City class is created. """
        c = City()
        self.assertIsInstance(c, BaseModel)
        self.assertIsInstance(c, City)

    def test_attributes(self):
        """ Test that City class has the required attributes. """
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.state_id, "")
        self.assertEqual(c.name, "")
        self.assertEqual(c.__class__.__name__, "City")

    def test_str(self):
        """ Test that the str method has the correct output. """
        c = City()
        string = "[City] ({}) {}".format(c.id, c.__dict__)
        self.assertEqual(string, str(c))

    def test_inheritance(self):
        """ Test that City class inherits from BaseModel. """
        c = City()
        self.assertTrue(issubclass(type(c), BaseModel))
