#!/usr/bin/python3
""" Module containing State class. """
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """ Test cases for State class. """
    def setUp(self):
        """ Set up test environment. """
        self.state = State(name="California")

    def test_instance(self):
        """ Test State instance. """
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """ Test State class inheritance"""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attributes(self):
        """ Test State instance attributes. """
        self.assertEqual(self.state.name, "California")

    def test_string_representation(self):
        """ Test string representation of State instance. """
        expected = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected)

    # def test_save_reload_state(self):
    #     """ Test saving and reloading State instance. """
    #     storage = FileStorage()
    #     storage.new(self.state)
    #     storage.save()

    #     new_storage = FileStorage()
    #     new_storage.reload()

    #     loaded_state = new_storage.all()["State." + self.state.id]
    #     self.assertEqual(loaded_state.name, self.state.name)


if __name__ == '__main__':
    unittest.main()
