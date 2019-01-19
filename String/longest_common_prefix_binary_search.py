# find shortest string
# use binary search on the left substring
# if it matches, use bs on the right substring
def longest_common_prefix_binary_search(input_list):
    if len(input_list) == 0:
        return ''

    substr = _find_shortest_string(input_list)

    longest_prefix = _find_longest_substr(0, len(substr), input_list, [])

    return ''.join(longest_prefix)


def _find_longest_substr(low, high, input_list, longest_prefix):
    if high - low <= 0:
        return longest_prefix

    match_prefix = _is_match_substring(low, high, input_list)
    mid = low + int((high - low) / 2)

    print(low, mid, high, longest_prefix)

    # if left match, check right
    if match_prefix:
        longest_prefix.append(input_list[0][low:high])
        return _find_longest_substr(high, high + high - low + 1, input_list, longest_prefix)
    else:
        # check low to mid
        return _find_longest_substr(low, mid, input_list, longest_prefix)

def _is_match_substring(low, high, input_list):
    substr = input_list[0][low: high]

    for word in input_list:
        if substr != word[low: high]:
            return False

    return True


def _find_shortest_string(input_list):
    length = len(input_list[0])
    substr = input_list[0]

    for word in input_list:
        if len(word) < length:
            length = len(word)
            substr = word

    return substr