def remove_duplicates(arr):
    length = len(arr)
    unique_index = 0

    for i in range(0, length - 1):
        if arr[i] != arr[i + 1]:
            arr[unique_index] = arr[i]
            unique_index += 1

    arr[unique_index] = arr[length - 1]

    return unique_index + 1
