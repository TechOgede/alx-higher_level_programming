#!/usr/bin/python3
''' This module defiens a function that an object to a textfile
    using JSON representation '''


def save_to_json_file(my_obj, filename):
    ''' Writes the JSON string of an object to file
        Args:
            my_obj: any serialisable Python Object
            filename: name of file
        '''
    import json
    with open(filename, "w", encoding='utf-8') as f:
        obj_json = json.dumps(my_obj)
        f.write(obj_json)
