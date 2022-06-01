#!/usr/bin/python3
import json

""" file Comments """


def save_to_json_file(my_obj, filename):

    """ function Comments """

    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
