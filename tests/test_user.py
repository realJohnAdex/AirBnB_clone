#!/usr/bin/python3
"""This module contains the User class test cases."""
import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """ Test cases for User class. """
    def setUp(self):
        """ Set up test environment. """
        self.user = User(email="test@example.com",
                         password="password123",
                         first_name="John",
                         last_name="Doe")

    def test_instance(self):
        """ Test User instance. """
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """ Test User class inheritance"""
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        """ Test User instance attributes. """
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_string_representation(self):
        """ Test string representation of User instance. """
        expected = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected)

    # def test_save_reload_user(self):
    #     """ Test saving and reloading User instance. """
    #     storage = FileStorage()
    #     storage.new(self.user)
    #     storage.save()

    #     new_storage = FileStorage()
    #     new_storage.reload()

    #     loaded_user = new_storage.all()["User." + self.user.id]
    #     self.assertEqual(loaded_user.email, self.user.email)
    #     self.assertEqual(loaded_user.password, self.user.password)
    #     self.assertEqual(loaded_user.first_name, self.user.first_name)
    #     self.assertEqual(loaded_user.last_name, self.user.last_name)


if __name__ == '__main__':
    unittest.main()
