#!/usr/bin/python3

""" file Comments """


def add_attribute(cls, field, value):

    """ function Commnets """

    if hasattr(cls, '__class__'):
        setattr(cls, field, value)
    else:
        raise TypeError("can't add new attribute")
