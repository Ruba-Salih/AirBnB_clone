#!/usr/bin/python3
"""Defines the FileStorage class."""
from models.base_model import BaseModel
import json


class FileStorage:
    """FileStorage calass that serializes and deserializes a JSON file"""

    __file_path = ''
    __objects = {}

    def all(self):
        """
        Returns: the dictionary __objects
        """

        return __class__.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        Args:
            obj: a class object
        """
        __class__.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """
            serializes __objects to the JSON file
        """
        dic_ob = __class__.__objects
        obj_dic = {i: dic_ob[i].to_dict() for i in dic_ob.keys()}
        with open(__class__.__file_path, 'w') as f:
            json.dump(obj_dic, f)

    def reload(self):
        """
            deserializes the JSON file to __objects
        """

        try:
            with open(__class__.__file_path, 'r') as f:
                dic_ob = json.load(f)
                for i in dic_ob.values():
                    cls_name = i["__class__"]
                    del i["__class__"]
                    self.new(eval(cls_name)(**i))

        except FileNotFoundError:
            pass
