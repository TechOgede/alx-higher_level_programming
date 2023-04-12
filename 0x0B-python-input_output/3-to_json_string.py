#!/usr/bin/python3
''' This module defines a function that serialises a string object '''


def to_json_string(my_obj):
    ''' Takes in a string and returns its JSON form '''
    import json
    return json.dumps(my_obj)
