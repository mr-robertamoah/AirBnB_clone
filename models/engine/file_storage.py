#!/usr/bin/python3

"""
this is a module containg the FileStorage class
"""

import uuid
import os
import json
from datetime import datetime
from models.base_model import BaseModel


class FileStorage():
    """
    FileStorage which will serve as the class that handles the persistence
    of objects into json files
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """  returns the dictionary __objects """

        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        key = str(obj.__class__.__name__) + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        with open(FileStorage.__file_path, "w") as file:
            objects_dict = {}
            for key, value in FileStorage.__objects.items():
                objects_dict[key] = FileStorage.__objects[key].to_dict()
            json.dump(objects_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file:
            content = file.read()
            if content is None:
                return
            objects_dict = json.loads(content)
            FileStorage.__objects = {}
            for key, value in objects_dict.items():
                FileStorage.__objects[key] = BaseModel(**objects_dict[key])
