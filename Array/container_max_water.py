def find_container_max_water(arr):
    left_index = 0
    right_index = len(arr) - 1

    left = build_left_height(arr)
    right = build_right_height(arr)

    return calc_max_water(arr, left, right, left_index, right_index)

def build_left_height(arr):
    left = [0] * len(arr)
    left[0] = arr[0]
    for index in range(1, len(arr)):
        if arr[index] > left[index - 1]:
            left[index] = arr[index]
        else:
            left[index] = left[index - 1]

    return left


def build_right_height(arr):
    length = len(arr) - 1
    right = [0] * len(arr)
    right[length] = arr[length]
    for index in range(length - 1, -1, -1):
        if arr[index] > right[index + 1]:
            right[index] = arr[index]
        else:
            right[index] = right[index + 1]

    return right


def calc_max_water(arr, left, right, left_index, right_index):
    if left_index >= len(arr) or right_index <= 0:
        return 0

    capacity = (right_index - left_index) * min(left[left_index], right[right_index])

    if left[left_index] < right[right_index]:
        left_index += 1
    else:
        right_index -= 1

    return max(capacity, calc_max_water(arr, left, right, left_index, right_index))


def find_container_most_water(arr):
    max_capacity = 0
    left = 0
    right = len(arr) - 1
    while (left < right):
        capacity = (right - left) * min(arr[left], arr[right])
        max_capacity = max(capacity, max_capacity)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

    return max_capacity

