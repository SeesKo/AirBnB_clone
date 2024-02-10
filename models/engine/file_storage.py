#!/usr/bin/python3
"""
Module for the FileStorage class.
"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """File storage class for serializing and deserializing instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()

        with open(
            FileStorage.__file_path, mode="w", encoding="utf-8"
        ) as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(
                FileStorage.__file_path, mode="r", encoding="utf-8"
            ) as file:
                deserialized_objects = json.load(file)
                for key, value in deserialized_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = eval(class_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
