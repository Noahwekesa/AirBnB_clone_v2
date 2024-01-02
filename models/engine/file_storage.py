#!/usr/bin/python3
"""
This module defines the FileStorage class, which serializes objects/instances
to a JSON file and deserializes JSON files to objects/instances. It also
imports the necessary classes from the models package.
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    a class that serializes object to a JSON file and
    deserializes JSON file to objects
    """

    __file_path = 'file.json'
    __objects = {}
    ClassName = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    def all(self):
        """
        the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
       program that sets in __objects the obj with key <obj class name>.id
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serialize __objects to the JSON file (path: __file_path).
        new_dict is a new dictionary in which the objects/instances
        have been replaced by their respective dictionary representation
        using the to_dict method from BaseModel.
        """
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            new_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """
        program that deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, 'r') as f:
                f_contents = f.read()
                dict_obj_dicts = json.loads(f_contents)
            for key in dict_obj_dicts.keys():
                obj_dict = dict_obj_dicts[key]
                # FileStorage.__objects[key] = BaseModel(**obj_dict)
                FileStorage.__objects[key] = FileStorage\
                           .className[key.split('.')[0]](**obj_dict)
        except FileNotFoundError:
            pass


def delete(self, obj=None):
    """
deletes a given object from __objects. if it exists
    """
    try:
        del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
    except (AttributeError, KeyError):
        pass


def close(self):
    """
calls the reload method
    """
    self.reload()
