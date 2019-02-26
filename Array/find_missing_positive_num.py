def find_missing_pos_num(arr):
    arr.append(0)
    if len(arr) == 0:
        return 1

    for i in range(0, len(arr)):
        if arr[i] < 0:
            arr[i] = 0

    for i in range(0, len(arr)):
        if abs(arr[i]) < len(arr):
            if arr[abs(arr[i])] > 0:
                arr[abs(arr[i])] = arr[abs(arr[i])] * -1

            if arr[abs(arr[i])] == 0:
                arr[abs(arr[i])] = abs(arr[i]) * -1

    for i in range(1, len(arr)):
        if arr[i] >= 0:
            return i

    return i + 1