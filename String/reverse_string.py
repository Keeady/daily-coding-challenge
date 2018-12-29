def reverse_words(str):
    str_arr = list(str)
    left = 0
    right = len(str) - 1
    reversed_chars = reverse_chars(str_arr, left, right)

    left = 0
    i = 0

    print(reversed_chars)
    for char in reversed_chars:
        right = i
        if char == ' ' or i == len(str) - 1:
            if char == ' ':
                right -= 1
            reverse_chars(str_arr, left, right)
            left = i + 1
        i += 1

    return ''.join(str_arr)


def reverse_chars(str_arr, left, right):
    while left < right:
        temp = str_arr[left]
        str_arr[left] = str_arr[right]
        str_arr[right] = temp
        left += 1
        right -= 1

    return str_arr