#!/usr/bin/python3

""" file Comments """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """ class Comments """

    def __init__(self, size):
        super().integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def area(self):
        return self.__size**2
