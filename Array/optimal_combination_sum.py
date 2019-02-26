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
    left = []
    right = []

    i = 0
    j = len(arr2) - 1

    while i < len(arr1):
        left = arr1[i]
        while j >= 0:
            right = arr2[j]
            temp_total = left[1] + right[1]
            if temp_total <= target:
                if temp_total > max_total:
                    max_total = temp_total
                    output = []
                    output.append([left[0], right[0]])
                elif temp_total == max_total:
                    output.append([left[0], right[0]])
                else:
                    i += 1
                    break
            else:
                j -= 1
        i += 1

    return output

