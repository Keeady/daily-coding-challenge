def is_unique(str):
    # cannot use additional data structure, so using loops
    # otherwise if ascii, use array of size 128 and check for ord() to find char index in array
    # if entry in array already set, return false otherwise set boolean

    # otherwise user hashmap, if in hashmap return false, otherwise add into hashmap

    length = len(str.strip())

    if length <= 1:
        return True

    for i in range(length):
        for j in range(length):
            if i == j:
                continue

            # case insensitive
            if str[i].lower() == str[j].lower():
                return False

    return True

def is_unique_sort(str):
    # sort the string and assume O(nlgn)
    # if allowed to modify string
    chars = list(str.strip().lower())
    length = len(chars)
    chars.sort()

    for i in range(length - 1):
        if chars[i].lower() == chars[i + 1].lower():
            return False

    return True