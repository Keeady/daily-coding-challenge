def zero_matrix(matrix):
    row_count = len(matrix)
    col_count = len(matrix[0])
    hasZeroRow = False
    hasZeroCol = False

    for row in range(0, row_count):
        if matrix[row][0] == 0:
            hasZeroRow = True
            break

    for col in range(0, col_count):
        if matrix[0][col] == 0:
            hasZeroCol = True
            break

    for row in range(1, row_count):
        for col in range(1, col_count):
            if matrix[row][col] == 0:
                if matrix[0][col] != 0:
                    matrix[0][col] = 0

                if matrix[row][0] != 0:
                    matrix[row][0] = 0

    for row in range(1, row_count):
        for col in range(1, col_count):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0


    if hasZeroRow == True:
        for row in range(0, row_count):
            matrix[row][0] = 0

    if hasZeroCol == True:
        for col in range(0, col_count):
            matrix[0][col] = 0

    return matrix