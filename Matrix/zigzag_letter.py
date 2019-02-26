def zigzag(str, num_rows):
    i = 0
    output = []

    while i < num_rows:
        output.append([])
        i += 1


    i = 0
    while i < len(str):
        row = i
        max_row = row + num_rows
        col = 0
        while row < max_row and row < len(str):
            output[col].append(str[row])
            row += 1
            col += 1

        col = num_rows - 2
        while col > 0 and row < len(str):
            output[col].append(str[row])
            col -= 1
            row += 1

        i = row


    i = 0
    while i < num_rows:
        output[i] = ''.join(output[i])
        i += 1

    return ''.join(output)
