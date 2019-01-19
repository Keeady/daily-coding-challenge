def is_permutation(str1, str2):
    # assume case insensitive
    # assume space not valid

    length = len(str1.strip())

    if length != len(str2.strip()):
        return False

    char_dict = {}
    for i in range(length):
        count = 0

        char = str1[i].lower()
        if char in char_dict:
            count += char_dict[char]

        count += 1
        char_dict[char] = count

    # iterate the str to see if in dict
    for i in range(length):
        char = str2[i].lower()
        if char not in char_dict:
            return False

        count = char_dict[char]

        if count <= 0:
            return False

        char_dict[char] = count - 1

    # iterate over dict if missed count
    values = list(char_dict.values())
    for i in values:
        if values[i] > 0:
            return False

    return True
