def calc_min_path_sum(matrix):
    '''
    [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    '''

    '''
    [
        [1,4,5],
        [2,8,6
        [6,8,7
    ]
    
    '''

    if len(matrix) == 0:
        return 0

    row = len(matrix)
    col = len(matrix[0])

    print(row, col)

    for i in range(1, col):
        matrix[0][i] = matrix[0][i] + matrix[0][i - 1]

    for i in range(1, row):
        matrix[i][0] = matrix[i][0] + matrix[i - 1][0]

    for i in range(1, row):
        for j in range(1, col):
            matrix[i][j] = min(matrix[i][j - 1], matrix[i - 1][j]) + matrix[i][j]

    return matrix[row - 1][col - 1]