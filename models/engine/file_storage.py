#!/usr/bin/python3
"""
Module for the FileStorage class.
"""

import json
import importlib
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    File storage class for serializing and deserializing instances.
    """
    __file_path = "file.json"
    __objects = {}
    __class_mapping = None

    @classmethod
    def _initialize_class_mapping(cls):
        if cls.__class_mapping is None:
            cls.__class_mapping = {}
            for name, obj in cls._get_model_classes().items():
                cls.__class_mapping[name] = obj

    @staticmethod
    def _get_model_classes():
        models_module = importlib.import_module('models')
        return {name: cls for name, cls in models_module.__dict__.items()
                if isinstance(cls, type) and issubclass(cls, BaseModel)}

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

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as file:
                deserialized_objects = json.load(file)
                self._initialize_class_mapping()
                for key, value in deserialized_objects.items():
                    class_name, obj_id = key.split('.')
                    cls = self.__class_mapping.get(class_name)
                    if cls:
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj
                    else:
                        return
        except FileNotFoundError:
            pass
