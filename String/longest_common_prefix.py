#
def longest_common_prefix(input_list):
    if len(input_list) == 0:
        return ''

    length = 1
    substr = input_list[0][0:length]
    match_prefix = compare_substr(input_list, length, substr)

    while match_prefix == True:
        length += 1
        substr = input_list[0][0:length]
        match_prefix = compare_substr(input_list, length, substr)

    if match_prefix == False:
        length -= 1

    return '' if length == 0 else input_list[0][0:length]


def compare_substr(input_list, length, substr):
    for word in input_list:
        if len(word) < length or word[0:length] != substr:
            return False

    return True
