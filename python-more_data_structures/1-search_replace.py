#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if oldnum == search else oldnum for oldnum in my_list]
    return new_list
