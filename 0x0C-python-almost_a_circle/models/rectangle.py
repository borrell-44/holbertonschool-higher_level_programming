#!/usr/bin/python3

""" file Comments """

from models.base import Base


class Rectangle(Base):

    """ class Comments """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ init constructure """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ str constructure """
        string = "[Rectangle] (" + str(self.id) + ") "
        string += str(self.x) + "/" + str(self.y) + " - "
        string += str(self.width) + "/" + str(self.height)
        return string

    @property
    def width(self):
        """ width property """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ height property """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x property """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y property """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ area method """
        return self.height * self.width

    def display(self):
        """ display method """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """ update method """
        names = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, names[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ dictionary method """
        keys = ["id", "width", "height", "x", "y"]
        values = [self.id, self.width, self.height, self.x, self.y]
        dic = {}
        for i in range(len(keys)):
            dic.update({keys[i]: values[i]})
        return dic
