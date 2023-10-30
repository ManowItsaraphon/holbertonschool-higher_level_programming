#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    roman_dict = {
                    "I": 1,
                    "V": 5,
                    "X": 10,
                    "L": 50,
                    "C": 100,
                    "D": 500,
                    "M": 1000,
                 }
    total = 0

    prev_val = 0
    for symbol in roman_string:
        value = roman_dict[symbol]

        if value > prev_val:
            total = total + value - 2 * prev_val
        else:
            total = total + value
        prev_val = value
    return total
