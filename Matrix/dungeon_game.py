def calc_min_knight_health(matrix):
    '''
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    [
        [1,3,6]
        [5,8
        [12
    ]
    '''

    #-55 1

    row = len(matrix)
    col = len(matrix[0])

    if row == 0 or col == 0:
        return 1

    for i in range(1, col):
        matrix[0][i] += matrix[0][i - 1]

    for i in range(1, row):
        matrix[i][0] += matrix[i - 1][0]

    print(matrix)

    for i in range(1, row):
        for j in range(1, col):
            down = matrix[i - 1][j] + matrix[i][j]
            right = matrix[i][j - 1] + matrix[i][j]

            if down <= 0:
                min_health_1 = abs(down) + 1
            else:
                min_health_1 = down

            if right <= 0:
                min_health_2 = abs(right) + 1
            else:
                min_health_2 = right

            matrix[i][j] = down if min_health_1 < min_health_2 else right

    remain = matrix[row - 1][col - 1]

    if remain > 0:
        return 1

    return abs(remain) + 1