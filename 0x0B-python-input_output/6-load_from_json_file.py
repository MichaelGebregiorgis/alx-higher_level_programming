#!/usr/bin/python3
"""Json"""
import json


def load_from_json_file(filename):
    """object from json"""
    with open(filename) as o:
        return json.load(o)
