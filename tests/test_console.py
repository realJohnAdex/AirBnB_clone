#!/usr/bin/python3
""" module for command interpreter tests"""
import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestConsole(unittest.TestCase):
    """ Test cases for the console module"""

    def setUp(self):
        """ Set up for the tests"""
        self.console = HBNBCommand()

    def tearDown(self):
        """ Clean up after each test"""
        # Specify the file path
        file_path = "file.json"

        # Check if the file exists
        if os.path.exists(file_path):
            # Remove the file
            os.remove(file_path)

    def test_create(self):
        """ Test the create command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertTrue(f.getvalue() != "")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertTrue(f.getvalue() != "")

    def test_show(self):
        """ Test the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** no instance found **\n")

    def test_destroy(self):
        """ Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy State")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy City")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Amenity")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Place")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy Review")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** no instance found **\n")

    def test_all(self):
        """ Test the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Amenity")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Review")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")

    def test_update(self):
        """ Test the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update State")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update City")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Amenity")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Place")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update Review")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** no instance found **\n")

    def test_quit(self):
        """ Test the quit command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit") is True)

    def test_EOF(self):
        """ Test the EOF command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF") is True)

    def test_emptyline(self):
        """ Test the emptyline command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("") is None)

    def test_create_instance(self):
        """ Test the create instance command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Place")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Review")
            self.assertTrue(f.getvalue() == "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("BaseModel 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("User 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("State 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("City 1234-1234-1234")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("Amenity 1234-123")
            self.assertTrue(f.getvalue() == "** class doesn't exist **\n")
