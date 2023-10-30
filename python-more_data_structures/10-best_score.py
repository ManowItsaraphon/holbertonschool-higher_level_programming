#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    highest = None
    highest_key = None
    for key in a_dictionary:
        if highest is None or a_dictionary[key] > highest:
            highest = a_dictionary[key]
            highest_key = key
    return highest_key
