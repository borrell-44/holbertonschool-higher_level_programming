#!/usr/bin/python3

""" file Comments """


def inherits_from(obj, a_class):

    """ function Comments """

    return issubclass(type(obj), a_class) and not type(obj) is a_class
