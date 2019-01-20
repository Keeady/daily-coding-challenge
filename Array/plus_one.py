def plus_one(arr):
    i = len(arr) - 1
    carry = 1

    while i >= 0:
        sum = arr[i] + carry
        carry = 0

        if sum >= 10:
            arr[i] = sum - 10
            carry = 1
        else:
            arr[i] = sum
        i -= 1

    if carry > 0:
        arr.insert(0, carry)

    return arr