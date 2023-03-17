#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    index = new_list.index(search)
    new_list.insert(index, replace)
    new_list.remove(search)
    return (new_list)
