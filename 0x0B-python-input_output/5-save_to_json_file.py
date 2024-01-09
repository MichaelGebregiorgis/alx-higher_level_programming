#!/usr/bin/python3
"""Json"""
import json


def save_to_json_file(my_obj, filename):
    """object to text file"""
    with open(filename, 'w') as w:
        json.dump(my_obj, w)
