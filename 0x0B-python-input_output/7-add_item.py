#!/usr/bin/python3
"""Add to python list"""
import sys

if __name__ == "__main__":
    load_file =\ __import__('6-load_from_json_file').load_from_json_file
    save_file = __import__('5-save_to_json_file').save_to_json_file

    try:
        val = load_file("add_item.json")
    except FileNotFounfError:
        val = []
    val.extend(sys.argv[1:])
    save_file(val, "add_item.json")
