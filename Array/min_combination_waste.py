import sys

def find_min_waste(input_array, qty, min_waste):
    matches = []

    matches.append(find_max_match(qty, input_array))
    matches.extend(find_min_matches(qty, input_array))

    print(qty, matches, sep=':')

    for m in matches:
        diff = m - qty
        if diff == 0:
            return 0
        # diff positive, larger bottle, diff is waste
        elif diff > 0:
            min_waste = min(min_waste, diff)
        else:
            min_waste = min(find_min_waste(matches, abs(diff), min_waste), min_waste)

    return min_waste


def find_max_match(qty, input_array):
    max = input_array[0]
    min_diff = sys.maxsize

    for value in input_array:
        if value > qty and value - qty  < min_diff:
            max = value

    return max

def find_min_matches(qty, input_array):
    comb = []
    for value in input_array:
        if value < qty:
            comb.append(value)

    return comb