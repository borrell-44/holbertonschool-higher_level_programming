#!/usr/bin/python3

"""" file Comments """

import json


def load_from_json_file(filename):

    """ function Comments """

    with open(filename) as f:
        return json.load(f)
