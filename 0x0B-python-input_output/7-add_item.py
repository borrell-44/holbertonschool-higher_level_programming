#!/usr/bin/python3

""" file Comments """

import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    list = load_from_json_file("add_item.json")
except Exception:
    list = []

for i in range(1, len(sys.argv)):
    list.append(sys.argv[i])

save_to_json_file(list, "add_item.json")
