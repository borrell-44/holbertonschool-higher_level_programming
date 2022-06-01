#!/usr/bin/python3
import json

""" file Comments """


def load_from_json_file(filename):

    """ function Comments """

    with open(filename) as f:
        return json.load(f)
