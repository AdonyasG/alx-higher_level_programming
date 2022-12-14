#!/usr/bin/python3
"""
Module - Base
"""


import json
import csv
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
        """ serializes and deserializes in CSV """
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as csvfile:
            wr = csv.writer(csvfile)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    wr.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == "Square":
                    wr.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        """ load csv file """
        obj = []
        filename = cls.__name__ + ".csv"
        if os.path.isfile(filename):
            with open(filename, 'r', newline='') as f:
                c_read = csv.reader(f)
                for row in c_read:
                    if cls.__name__ == "Rectangle":
                        names = {"id": int(row[0]), "width": int(row[1]),
                                 "height": int(row[2]), "x": int(row[3]),
                                 "y": int(row[4])}
                    if cls.__name__ == "Square":
                        names = {"id": int(row[0]), "size": int(row[1]),
                                 "x": int(row[2]), "y": int(row[3])}
                    link = cls.create(**names)
                    obj.append(link)
        return obj
