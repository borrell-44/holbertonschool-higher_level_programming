#!/usr/bin/python3
import json

""" file Comments """


def from_json_string(my_obj):

    """ function Comments """

    dic = json.dumps(my_obj)
    return json.loads(my_obj)
