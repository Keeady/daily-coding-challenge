def add_binary(a, b):
    #11
    #10
    output = []

    pointerA = len(a) - 1
    pointerB = len(b) - 1
    insert_index = 0
    carry = 0


    while pointerA >= 0 or pointerB >= 0:
        if pointerA < 0:
            valA = '0'
        else:
            valA = a[pointerA]

        if pointerB < 0:
            valB = '0'
        else:
            valB = b[pointerB]

        sum = carry # 1 or 0
        sum += 1 if valA == '1' else 0
        sum += 1 if valB == '1' else 0


def _calc_binary(output, valA, valB):
    if valA == '0' and valB == '0':
        return 0

    elif valA == '1' and valB == '0' or valA == '0' and valB == '1':
        return 1

    else:
        return 10
