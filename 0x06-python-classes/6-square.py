#!/usr/bin/python3

""" File Comments """


class Square(object):

    """ class Comments """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) == 2 or type(value) == int:
            if value[0] > 0 or value[1] > 0:
                self.__position = value
                pass
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size**2

    def my_print(self):
        if self.__size == 0:
            print()
        num = self.__size
        for i in range(num):
            for j in range(num):
                print("#", end="")
            print()
