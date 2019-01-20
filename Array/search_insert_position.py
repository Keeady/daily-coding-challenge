def search_insert_position(arr, value):
    left = 0
    right = len(arr) - 1

    if value > arr[right]:
        return right + 1

    if value < arr[left]:
        return left

    return _search_binary_search(arr, value, left, right)


def _search_binary_search(arr, value, low, high):
    if high - low <= 0:
        return low

    mid = low + int((high - low) / 2)

    if value < arr[mid]:
        return _search_binary_search(arr, value, low, mid)

    elif value > arr[mid]:
        return _search_binary_search(arr, value, mid + 1, high)

    return mid