#!/usr/bin/python3

""" file Comments """


class Student(object):

    """ class Comments """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        hold = self.__dict__
        if attrs is not None:
            dic = {k: hold[k] for k in hold.keys() & attrs}
            return dic
        return hold
