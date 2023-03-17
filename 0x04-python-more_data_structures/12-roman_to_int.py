#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    num = 0
    i = 0
    r_nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman = roman_string.upper()
    while i < len(roman):
        curr = roman[i]
        if (i + 1 < len(roman)):
            next_r = roman[i + 1]
            if r_nums[curr] < r_nums[next_r]:
                num += (r_nums[next_r] - r_nums[curr])
                i += 2
            else:
                num += r_nums[curr]
                i += 1
        else:
            num += r_nums[curr]
            i += 1

    return num
