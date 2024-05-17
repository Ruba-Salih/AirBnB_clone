#!/usr/bin/python3
"""
BaseModel class definition
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class  defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """

        self.id = '{}'.format(uuid4())
        self.created_at = self.updated_at = datetime.today()

        frt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    val = datetime.strptime(val, frt)
                if key != "__class__":
                    setattr(self, key, val)
        

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """

        self.updated_at = datetime.today()

    def __str__(self):
        """
        Return: class name and it's attributes
        """

        name = self.__class__.__name__
        return f"[{name}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """
        Return: returns a dictionary containing all keys/values
        """

        base_dic = self.__dict__.copy()
        base_dic.update({"__class__": self.__class__.__name__})
        base_dic["created_at"] = self.created_at.isoformat()
        base_dic["updated_at"] = self.updated_at.isoformat()

        return base_dic
