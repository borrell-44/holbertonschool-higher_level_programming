#!/usr/bin/python3

""" file Comments """


class BaseGeometry():

    """ class Comments """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(name + " must be an integer")

        if value < 1:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):

    """ class Comments """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width

        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def __str__(self):
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string

    def area(self):
        return self.__width * self.__height


class Square(Rectangle):

    """ class Rectangle """

    def __init__(self, size):
        BaseGeometry.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        width = str(self.__size)
        height = str(self.__size)
        string = "[Square] " + width + "/" + height
        return string

    def area(self):
        return self.__size**2
