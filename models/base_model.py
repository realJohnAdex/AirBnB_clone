#!/usr/bin/python3
"""
Module containing BaseModel class.
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    BaseModel class defining common attributes/methods for other classes.
    """
    def __init__(self, **kwargs):
        """
        Initializes a BaseModel instance.

        Args:
            *args: Unused.
            **kwargs: Dictionary representation of BaseModel instance.
        """
        if kwargs:
            if 'id' not in kwargs:
                kwargs['id'] = str(uuid.uuid4())
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'],
                    "%Y-%m-%dT%H:%M:%S.%f")
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'],
                    "%Y-%m-%dT%H:%M:%S.%f")
            kwargs.pop('__class__', None)  # Remove '__class__' key if present
            self.__dict__.update(kwargs)
        else:
            from models import storage

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns string representation of BaseModel instance.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns dictionary representation of BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
