#!/usr/bin/python3
"""
Module - Base
"""


import json
import os


class Base:
    """class base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initilaize"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of list dict"""
        if list_dictionaries is None or len(list_dictionaries) == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs to a file"""
        i = []
        if list_objs is not None:
            for j in list_objs:
                i.append(cls.to_dictionary(j))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(i))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Square":
                dummy = cls(1)
            if cls.__name__ == "Rectangle":
                dummmy = cls(1, 1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        new = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                dic = Base.from_json_string(f.read())
                for i in dic:
                    new.append(cls.create(**i))
                return new
        except Exception:
            return []
