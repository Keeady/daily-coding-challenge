def is_palindrome_permutation(str):
    # store character count in dict

    # iterate over dict % 2
    # if 0 T else F
    count_dict = {}
    for char in str:
        count = 0
        if char == ' ':
            continue

        if char.lower() in count_dict:
            count = count_dict[char.lower()]

        count += 1
        count_dict[char.lower()] = count

    print(count_dict)
    odd = False
    for char in count_dict:
        if count_dict[char] % 2 == 1:
            if odd is True:
                return False
            else:
                odd = True

    return True