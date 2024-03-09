#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_instantiation(self):
        """Test for Review class"""
        r = Review()
        self.assertIsInstance(r, BaseModel)
        self.assertIsInstance(r, Review)

    def test_attributes(self):
        """Test for Review attributes"""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertTrue(hasattr(r, "user_id"))
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.place_id, "")
        self.assertEqual(r.user_id, "")
        self.assertEqual(r.text, "")
        self.assertEqual(r.__class__.__name__, "Review")

    def test_str(self):
        """Test for Review __str__ method"""
        r = Review()
        string = "[Review] ({}) {}".format(r.id, r.__dict__)
        self.assertEqual(string, str(r))

    def test_inheritance(self):
        """Test for Review inheritance"""
        r = Review()
        self.assertTrue(issubclass(type(r), BaseModel))
