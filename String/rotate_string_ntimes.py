def rotate(str, n):
    #
    if n == len(str) or len(str) <= 1:
        return str

    arr = list(str)

    if n > len(str):
        n %= len(str)

    reverse(arr, 0, n - 1)
    reverse(arr, n, len(str) - 1)
    reverse(arr, 0, len(str) - 1)

    return ''.join(arr)


def reverse(arr, start, end):
    while start < end:
        buffer = arr[start]
        arr[start] = arr[end]
        arr[end] = buffer

        start += 1
        end -= 1
    return arr


def smart_rotate(str, n):
    if n == len(str) or len(str) <= 1:
        return str

    arr = list(str)

    if n > len(str):
        n %= len(str)

    insert = 0
    for i in range(n, len(str)):
        arr[insert] = str[i]
        insert += 1

    for i in range(0, n):
        arr[insert] = str[i]
        insert += 1

    return ''.join(arr)
