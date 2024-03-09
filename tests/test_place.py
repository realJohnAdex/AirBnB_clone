#!/usr/bin/python3
""" Module for testing Place class. """

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Tests for Place class. """

    def test_instance(self):
        """ Test if Place is an instance of BaseModel. """
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)
        self.assertIsInstance(new_place, Place)

    def test_attributes(self):
        """ Test if Place has the required attributes. """
        new_place = Place()
        self.assertTrue(hasattr(new_place, "city_id"))
        self.assertTrue(hasattr(new_place, "user_id"))
        self.assertTrue(hasattr(new_place, "name"))
        self.assertTrue(hasattr(new_place, "description"))
        self.assertTrue(hasattr(new_place, "number_rooms"))
        self.assertTrue(hasattr(new_place, "number_bathrooms"))
        self.assertTrue(hasattr(new_place, "max_guest"))
        self.assertTrue(hasattr(new_place, "price_by_night"))
        self.assertTrue(hasattr(new_place, "latitude"))
        self.assertTrue(hasattr(new_place, "longitude"))
        self.assertTrue(hasattr(new_place, "amenity_ids"))
        self.assertEqual(new_place.city_id, "")
        self.assertEqual(new_place.user_id, "")
        self.assertEqual(new_place.name, "")
        self.assertEqual(new_place.description, "")
        self.assertEqual(new_place.number_rooms, 0)
        self.assertEqual(new_place.number_bathrooms, 0)
        self.assertEqual(new_place.max_guest, 0)
        self.assertEqual(new_place.price_by_night, 0)
        self.assertEqual(new_place.latitude, 0.0)
        self.assertEqual(new_place.longitude, 0.0)
        self.assertEqual(new_place.amenity_ids, [])

    def test_str(self):
        """ Test the str method has the correct output. """
        new_place = Place()
        string = "[Place] ({}) {}".format(new_place.id, new_place.__dict__)
        self.assertEqual(string, str(new_place))

    def test_inheritance(self):
        """ Test that Place class inherits from BaseModel. """
        new_place = Place()
        self.assertTrue(issubclass(type(new_place), BaseModel))

    def test_to_dict(self):
        """ Test that to_dict method has the correct output. """
        new_place = Place()
        place_dict = new_place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIsInstance(place_dict["created_at"], str)
        self.assertIsInstance(place_dict["updated_at"], str)
        self.assertIsInstance(place_dict["id"], str)
        self.assertEqual(place_dict["__class__"], "Place")
