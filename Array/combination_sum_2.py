def calc_comb(arr, target):
    return helper(0, 0, arr, [], [], target)


def helper(index, total, arr, temp, output, target):
    if total == target:
        output.append([x for x in temp])
    else:
        for i in range(index, len(arr)):
            num = arr[i]
            if total + num <= target:
                temp.append(num)
                helper(i, total + num, arr, temp, output, target)
                temp.pop()

    return output