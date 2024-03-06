#!/usr/bin/python3
"""
Unit tests for BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel class.
    """
    def test_instance_creation(self):
        """
        Test instance creation of BaseModel class.
        """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)

    def test_id_is_string(self):
        """
        Test id attribute type of BaseModel class.
        """
        b = BaseModel()
        self.assertIsInstance(b.id, str)

    def test_created_at_is_datetime(self):
        """
        Test created_at attribute type of BaseModel class.
        """
        b = BaseModel()
        self.assertIsInstance(b.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test updated_at attribute type of BaseModel class.
        """
        b = BaseModel()
        self.assertIsInstance(b.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """
        Test save method updates updated_at attribute of BaseModel class.
        """
        b = BaseModel()
        original_updated_at = b.updated_at
        b.save()
        self.assertNotEqual(original_updated_at, b.updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test to_dict method returns dictionary representation of BaseModel class.
        """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)

    def test_to_dict_contains_class_name(self):
        """
        Test to_dict method includes '__class__' key with class name in dictionary representation.
        """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIn('__class__', b_dict)
        self.assertEqual(b_dict['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        """
        Test to_dict method includes 'created_at' key in dictionary representation.
        """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIn('created_at', b_dict)

    def test_to_dict_contains_updated_at(self):
        """
        Test to_dict method includes 'updated_at' key in dictionary representation.
        """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIn('updated_at', b_dict)

    def test_to_dict_created_at_format(self):
        """
        Test to_dict method returns 'created_at' attribute in proper ISO format.
        """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict['created_at'], str)

    def test_to_dict_updated_at_format(self):
        """
        Test to_dict method returns 'updated_at' attribute in proper ISO format.
        """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()