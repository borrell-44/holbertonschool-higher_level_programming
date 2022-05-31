#!/usr/bin/python3

""" file Comments """


class BaseGeometry(object):

    """ class Comments """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value < 1:
            raise ValueError(name + " must be greater than 0")
