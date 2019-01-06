from Matrix import rotate_matrix_90_clockwise


def test_rotate_matrix_90():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [[7,4,1],[8,5,2],[9,6,3]]

    assert output == rotate_matrix_90_clockwise.rotate_image_90(matrix)

    matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    output = [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]]

    assert output == rotate_matrix_90_clockwise.rotate_image_90(matrix)

def test_rotate_matrix():
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [[7,4,1],[8,5,2],[9,6,3]]

    assert output == rotate_matrix_90_clockwise.rotate_image_matrix(matrix)

    matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    output = [[15,13, 2, 5],[14, 3, 4, 1],[12, 6, 8, 9],[16, 7,10,11]]

    assert output == rotate_matrix_90_clockwise.rotate_image_matrix(matrix)
