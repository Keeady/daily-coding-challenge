def sums(arr):
    sum_dict = {}
    output = []
    for index in range(0, len(arr)):
        #a + b + c = 0
        #a + b = -c
        if arr[index] in sum_dict:
            out = sum_dict[arr[index]]
            out.append(arr[index])
            output.append(out)
            continue

        two_sum(arr, index, sum_dict)

    return output


def two_sum(arr, index, sum_dict):
    for i in range(0, len(arr)):
        if i != index:
            # a +b = -c -b
            comp = arr[index] * -1 - arr[i]
            sum_dict[comp] = [arr[index], arr[i]]

    return sum_dict