# a palindrome reads the same from left to right
# convert into a string
# use 2 pointers left, right
# false if pointers dont match
def is_palindrome(num):
    if num < 0:
        return False

    num_str = str(num)
    left = 0
    right = len(num_str) - 1

    while left < right:
        if num_str[left] != num_str[right]:
            return False
        left += 1
        right -= 1

    return True


# divide the number by each digit's divisor
# 232 for example
# divide 232/100 and 232%10 and compare the result
def is_palindrome_int(num):
    if num < 0:
        return False

    if num < 10:
        return True

    divisor = 10
    while num / divisor > 10:
        divisor *= 10

    left_divisor = divisor
    right_divisor = 10

    print(left_divisor, right_divisor)

    i = 0

    while left_divisor >= right_divisor:
        # modulo of 10 to get the last digit
        left = int(num / left_divisor) % 10

        # divide by the same length of power of 10 to get the desired digit
        # ex divide 213 by 100 to get 2
        # divide 13 by 10 to get 1
        right = int((num % right_divisor) / pow(10, i))

        print(left_divisor, right_divisor, left, right)

        if left != right:
            return False

        left_divisor = int(left_divisor / 10)
        right_divisor = right_divisor * 10
        i += 1

    return True