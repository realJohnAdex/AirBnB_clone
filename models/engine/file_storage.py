#!/usr/bin/python3
"""
Module containing FileStorage class.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Dictionary mapping class names to their corresponding class objects
CLASS_MAP = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    # Add other class names and their corresponding class objects here
}


class FileStorage:
    """
    FileStorage class for serializing instances to a JSON file
    and deserializing JSON file to instances.
    """
    __file_path = "file.json"
    __objects = {}

    def file_path(self):
        """
        Returns the file path to the JSON file.
        """
        return FileStorage.__file_path

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file.
        """
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for k, v in obj_dict.items():
                    class_name = v.pop('__class__', None)
                    if class_name:
                        obj_id = k.split('.')[1]
                        class_obj = CLASS_MAP.get(class_name)
                        if class_obj:
                            obj = class_obj(**v)
                            self.new(obj)
        except FileNotFoundError:
            pass
