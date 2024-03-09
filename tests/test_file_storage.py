#!/usr/bin/python3
"""
Unit tests for FileStorage class.
"""
import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage class.
    """
    def setUp(self):
        """
        Set up test environment.
        """
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up test environment.
        """
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_instance_creation(self):
        """
        Test instance creation of FileStorage class.
        """
        self.assertIsInstance(self.storage, FileStorage)

    def test_all_returns_dict(self):
        """
        Test all method returns a dictionary.
        """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """
        Test new method adds an object to __objects dictionary.
        """
        b = BaseModel()
        self.storage.new(b)
        key = "{}.{}".format(b.__class__.__name__, b.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """
        Test save and reload methods.
        """
        b1 = BaseModel()
        b2 = BaseModel()
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key1 = "{}.{}".format(b1.__class__.__name__, b1.id)
        key2 = "{}.{}".format(b2.__class__.__name__, b2.id)
        self.assertIn(key1, new_storage.all())
        self.assertIn(key2, new_storage.all())


if __name__ == '__main__':
    unittest.main()
