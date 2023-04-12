#!/usr/bin/python3
''' This module defiens a function that reads a JSON string from a file
    and deserialises it '''


def load_from_json_file(filename):
    ''' Reads a JSON string of an object from a  file
        Args:
            filename: name of file
        '''
    import json
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
