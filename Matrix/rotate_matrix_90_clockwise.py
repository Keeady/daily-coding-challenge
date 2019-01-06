def rotate_image_90(matrix):
    length = len(matrix)

    max_row = int(length / 2)
    max_col = length
    for row in range(0, max_row):
        for col in range(row, max_col - 1):

            new_row = col
            new_col = length - 1 - row
            buffer = matrix[new_row][new_col]
            matrix[new_row][new_col] = matrix[row][col]

            new_row2 = new_col
            new_col2 = length - 1 - new_row
            buffer2 = matrix[new_row2][new_col2]
            matrix[new_row2][new_col2] = buffer

            new_row3 = new_col2
            new_col3 = length - 1 - new_row2
            buffer3 = matrix[new_row3][new_col3]
            matrix[new_row3][new_col3] = buffer2

            matrix[row][col] = buffer3

        max_col -= 1

    return matrix

def rotate_image_matrix(matrix):
    length = len(matrix)
    max_row = length // 2 + length % 2
    temp = [0] * 4

    for row in range(0, max_row):
        for col in range(0, length//2):
            r = row
            c = col
            for k in range(1, 4):
                temp[k] = matrix[r][c]
                r, c = c,length - 1 - r
            temp[0] = matrix[r][c]

            r = row
            c = col
            for k in range(4):
                matrix[r][c] = temp[k]
                r, c = c, length - 1 - r

    return matrix

