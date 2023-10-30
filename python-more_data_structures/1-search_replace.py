#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = [replace if oldnumber == search else oldnumber for oldnumber in my_list]
    return new_list
