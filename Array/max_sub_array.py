# divide the array recursively into a left and right sub array
# until each sub array is just one element
# compare and select max between left or right or left+right

def find_max_sub_array(arr):
    return _max_sub_array(arr, 0, len(arr) - 1)

def _max_sub_array(arr, low, high):
    if high == low:
        return arr[low]

    mid = low + int((high - low) / 2)
    left = _max_sub_array(arr, low, mid)
    right = _max_sub_array(arr, mid + 1, high)
    cross = _max_cross_sub_array(arr, low, mid, high)

    if left >= right and left >= cross:
        return left
    elif right >= left and right >= cross:
        return right

    return cross

def _max_cross_sub_array(arr, low, mid, high):
    return _max_cross_sub_array_left(arr, low, mid) + _max_cross_sub_array_right(arr, mid + 1, high)

def _max_cross_sub_array_left(arr, low, mid):
    max_left_sum = float('-inf')
    i = mid
    sum = 0
    while i >= low:
        sum += arr[i]
        if sum > max_left_sum:
            max_left_sum = sum
        i -= 1

    return max_left_sum

def _max_cross_sub_array_right(arr, mid, high):
    max_right_sum = float('-inf')
    i = mid
    sum = 0
    while i <= high:
        sum += arr[i]
        if sum > max_right_sum:
            max_right_sum = sum
        i += 1

    return max_right_sum

