#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = max(a_dictionary.values())
    for k, v in a_dictionary.items():
        if v == max_val:
            return k
