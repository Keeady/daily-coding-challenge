# evaluate each roman char
# add left with right
# if left is less, then subtraction

def convert_roman_to_int(roman_num):
    sum = 0
    roman_int_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    return convert_seq(sum, 0, 1, roman_num, roman_int_dict)


def convert_seq(sum, left, right, roman_num, roman_int_dict):
    if right > len(roman_num):
        return sum

    if right > len(roman_num) - 1:
        sum += roman_int_dict[roman_num[left]]
        return sum

    value = roman_int_dict[roman_num[left]]
    next_value = roman_int_dict[roman_num[right]]
    if value < next_value:
        sum = sum + (next_value - value)
        return convert_seq(sum, right + 1, right + 2, roman_num, roman_int_dict)
    else:
        sum += value

    return convert_seq(sum, left + 1, right + 1, roman_num, roman_int_dict)