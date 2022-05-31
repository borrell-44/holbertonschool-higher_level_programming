#!/usr/bin/python3

""" file Comments """


def add_attribute(cls, field, value):

    """ function Commnets """

    try:
        setattr(cls, field, value)
    except Exception:
        raise TypeError("can't add new attribute")
