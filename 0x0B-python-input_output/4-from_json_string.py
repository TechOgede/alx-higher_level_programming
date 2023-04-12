#!/usr/bin/python3
''' This module defines a function that deserialises a JSON string '''


def from_json_string(my_str):
    ''' Takes in a JSON string and returns a Python Object '''
    import json
    return json.loads(my_str)
