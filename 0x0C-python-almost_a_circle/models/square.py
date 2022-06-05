#!/usr/bin/python3

""" file Comments """

from models.rectangle import Rectangle


class Square(Rectangle):

    """ class Comments """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        string = "[Square] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
        return string

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        names = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        keys = ["id", "size", "x", "y"]
        values = [self.id, self.size, self.x, self.y]
        dic = {}
        for i in range(len(keys)):
            dic.update({keys[i] : values[i]})
        return dic
