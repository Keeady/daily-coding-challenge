def count_unique_path(max_row, max_col):
    if max_row == 0 or max_col == 0:
        return 0

    matrix = [[0] * max_col for r in range(0, max_row)]

    for i in range(0, max_col):
        matrix[0][i] = 1

    for i in range(0, max_row):
        matrix[i][0] = 1

    for i in range(1, max_row):
        for j in range(1, max_col):
            matrix[i][j] = matrix[i][j - 1] + matrix[i - 1][j]

    return matrix[max_row - 1][max_col - 1]


def count(row, col, max_row, max_col):
    if row >= max_row or col >= max_col:
        return 0

    if row == max_row - 1 and col == max_col - 1:
        return 1

    return count(row + 1, col, max_row, max_col) + count(row, col + 1, max_row, max_col)


def count_dp(matrix, max_row, max_col, row, col):
    if row >= max_row or col >= max_col:
        return matrix

    # row, col - 1
    # row - 1, col
    matrix[row][col] = matrix[row][col-1] + matrix[row-1][col]

    count_dp(matrix, max_row, max_col, row + 1, col)
    count_dp(matrix, max_row, max_col, row, col + 1)

    return matrix