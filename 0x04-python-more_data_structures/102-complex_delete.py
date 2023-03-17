#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    list_keys = list(a_dictionary.keys())
    for key in list_keys:
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
