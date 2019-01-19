def urlify(str, l):
    # %20 is 3 characters long
    # each space in the string has only one space available, technically

    chars = list(str)

    # count spaces in string
    count = 0
    i = 0
    for char in chars:
        if char == ' ' and i < l:
            count += 1
        i += 1

    if count == 0:
        return str

    # final length of string including %20 for each count spaces
    j = l - count + (count * 3) - 1

    for i in range(l - 1, -1, -1):

        if chars[i] == ' ':
            chars[j] = '0'
            chars[j - 1] = '2'
            chars[j - 2] = '%'

            j -= 3
        else:
            chars[j] = chars[i]
            j -= 1

    return ''.join(chars)