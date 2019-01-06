from Matrix import zero_matrix


def test_zero_matrix():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    output = zero_matrix.zero_matrix(matrix)
    assert output == [[1,0,1],[0,0,0],[1,0,1]]

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    output = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    assert output == zero_matrix.zero_matrix(matrix)

    matrix = [[1,1,1],[0,0,0],[1,1,1]]
    output = [[0,0,0],[0,0,0],[0,0,0]]
    assert output == zero_matrix.zero_matrix(matrix)

    matrix = [[1,1,1],[1,1,1],[0,0,0]]
    output = [[0,0,0],[0,0,0],[0,0,0]]
    assert output == zero_matrix.zero_matrix(matrix)
