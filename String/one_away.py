def one_away(str1, str2):
    # same length or abs(diff(length1, length2)) <= 1
    diff = abs(len(str2) - len(str1))
    length = len(str1)
    if len(str1) > len(str2):
        length = len(str2)

    if diff > 1:
        return False

    odd = False
    index1 = 0
    index2 = 0
    for i in range(length):
        if index1 >= len(str1) or index2 >= len(str2):
            return True

        if str1[index1] != str2[index2]:
            if str1[index1 + 1] == str2[index2]:
                index1 += 1
            if str1[index1] == str2[index2 + 1]:
                index2 += 1

            if odd is False:
                odd = True
            else:
                return False

        index1 += 1
        index2 += 1

    return True