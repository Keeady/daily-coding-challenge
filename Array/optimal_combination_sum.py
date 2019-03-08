import queue


def find_optimal_combination(arr1, arr2, target):
    max_total = 0
    max_pairs = []

    for num1 in arr1:
        if num1 >= target:
            continue

        for num2 in arr2:
            if num2 >= target:
                continue

            temp = []
            # combine if pair don't exceed max
            temp_total = num1 + num2
            if temp_total <= target:
                if temp_total == max_total:
                    max_pairs.append([num1, num2])
                elif temp_total > max_total:
                    max_pairs = []
                    max_total = temp_total
                    max_pairs.append([num1, num2])

    return max_pairs


def find_combination_sum(arr1, arr2, target):
    arr1.sort(key=lambda x: x[1])
    arr2.sort(key=lambda x: x[1])

    output = []
    max_total = 0

    left = 0
    right = len(arr2) - 1

    visited_indices = {}

    queue_indices = queue.Queue()
    queue_indices.put((left, right))

    while not queue_indices.empty():
        pos = queue_indices.get()
        left = pos[0]
        right = pos[1]

        if left < 0 or left >= len(arr1) or right < 0 or right >= len(arr2):
            continue

        if pos in visited_indices:
            continue
        else:
            visited_indices[pos] = True

        total = arr1[left][1] + arr2[right][1]
        print(left, right, total)
        if total > max_total and total <= target:
            max_total = total
            output = []

        if total == max_total:
            output.append([arr1[left][0], arr2[right][0]])

        if total < target:
            queue_indices.put((left + 1, right))
            queue_indices.put((left, right + 1))
            queue_indices.put((left + 1, right + 1))

        elif total > target:
            queue_indices.put((left - 1, right))
            queue_indices.put((left, right - 1))
            queue_indices.put((left - 1, right - 1))

        else:
            queue_indices.put((left - 1, right + 1))
            queue_indices.put((left + 1, right - 1))

    return output