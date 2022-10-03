#!/usr/bin/python3
"""
Module - Base
"""


import json
import os


class Base():
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
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            if list_objs is None:
                f.write('[]')
            else:
                f.write(cls.to_json_string([o.to_dictionary()
                        for o in list_objs]))

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
        if (cls.__name__ == "Square"):
            dum = cls(4)
        if (cls.__name__ == "Rectangle"):
            dum = cls(4, 4)
        dum.update(**dictionary)
        return dum

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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save csv file"""
        if (list_objs is None):
            with open("{}.csv".format(cls.__name__), "w") as f:
                writer = csv.writer(f)
        else:
            new = []
            with open("{}.csv".format(cls.__name__), "w") as f:
                for obj in list_objs:
                    new.append(obj.to_dictionary())
                f.write(Base.to_json_string(new))
