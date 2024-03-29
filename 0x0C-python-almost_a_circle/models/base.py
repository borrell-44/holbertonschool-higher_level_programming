#!/usr/bin/python3

""" file Comments """

import json
import os


class Base(object):

    """ class Comments """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init constructure """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json_string static method """
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save_to_file class method """
        name = str(cls.__name__) + ".json"
        ls = []
        if list_objs is not None:
            for i in list_objs:
                ls.append(i.to_dictionary())
        with open(name, "w") as f:
            context = Base.to_json_string(ls)
            f.write(context)

    @staticmethod
    def from_json_string(json_string):
        """ from_json_string static method """
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create class method """
        if cls.__name__ == "Square":
            dum = cls(size=1)
        else:
            dum = cls(1, 1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """ load_from_file class method """
        name = str(cls.__name__) + ".json"
        ls = []
        if not os.path.isfile(name):
            return ls
        with open(name, "r") as f:
            content = f.read()
        dic = cls.from_json_string(content)
        for i in dic:
            ls.append(cls.create(**i))
        return ls

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save_to_file_csv class method """
        name = str(cls.__name__) + ".csv"
        ls = []
        if list_objs is not None:
            for i in list_objs:
                ls.append(i.to_dictionary())
        with open(name, "w") as f:
            context = Base.to_json_string(ls)
            f.write(context)

    @classmethod
    def load_from_file_csv(cls):
        """ load_from_file_csv class method """
        name = str(cls.__name__) + ".csv"
        ls = []
        if not os.path.isfile(name):
            return ls
        with open(name, "r") as f:
            content = f.read()
        dic = cls.from_json_string(content)
        for i in dic:
            ls.append(cls.create(**i))
        return ls
