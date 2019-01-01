def find_element(sorted_arr, el):
    low = 0
    high = len(sorted_arr) - 1

    if len(sorted_arr) == 0:
        return -1

    while low >= 0 and high <= len(sorted_arr) and low <= high:
        mid = low + int((high - low) / 2)

        if sorted_arr[mid] > el:
            # search in lower half
            high = mid - 1

        elif sorted_arr[mid] < el:
            # search in higher half
            low = mid + 1
        else:
            return mid

    return -1