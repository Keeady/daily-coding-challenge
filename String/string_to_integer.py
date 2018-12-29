def string_to_integer(str):
    str_arr = list(str)
    right = len(str) - 1
    sum = 0

    while right > 0:
        num = convert_string_to_integer(str_arr, right)
        print(num)
        sum = sum + num
        right -= 1

    char = convert_string_to_integer(str_arr, 0)
    if char == '-':
        sum *= -1
    else:
        sum += char

    return sum


def convert_string_to_integer(str_arr, index):
    if str_arr[index] != '-':
        return int(str_arr[index]) * pow(10, len(str_arr) - index - 1)

    return str_arr[index]