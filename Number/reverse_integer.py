# reverse the integer by converting to a string then to a list
# then reversing the list
# converting the list into a string
# converting the string to an int
def reverse_integer(num):
    num_str = str(num)
    num_list = list(num_str)

    left = 0
    right = len(num_list) - 1

    while left < right:
        if num_list[left] == '-':
            left += 1
            continue

        buffer = num_list[left]
        num_list[left] = num_list[right]
        num_list[right] = buffer

        left += 1
        right -= 1

    return int(''.join(num_list))


# reversing an integer by dividing the number by 10 until it's 0,
# moving its modulo into a reverse order
def reverse_int(num):
    reverse = 0
    flag = -1 if num < 0 else 1
    num *= flag

    while num > 0:
        remainder = num % 10
        reverse = reverse * 10 + remainder
        print(reverse)
        num = int(num / 10)
        print(num)

    return reverse * flag
