#!/usr/bin/python3

""" file Comments """

from models.rectangle import Rectangle


class Square(Rectangle):

    """ class Comments """

    def __init__(self, size, x=0, y=0, id=None):
        """ init constructure """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """ str constructure """
        string = "[Square] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width)
        return string

    @property
    def size(self):
        """ size property """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update method """
        names = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary method """
        keys = ["id", "size", "x", "y"]
        values = [self.id, self.size, self.x, self.y]
        dic = {}
        for i in range(len(keys)):
            dic.update({keys[i]: values[i]})
        return dic
