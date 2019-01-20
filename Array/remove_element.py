def remove_element(arr, value):
    insert_index = 0
    length = len(arr)

    for i in range(0, length):
        if arr[i] != value:
            arr[insert_index] = arr[i]
            insert_index += 1

    return insert_index