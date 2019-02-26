from Array import robot_in_grid


def test_grid():
    arr = [[0, 0],[0, 0]]
    assert 2 == robot_in_grid.count_move(arr, 2, 2)

    arr = [[0, 0, -1], [0, -1, 0], [0, 0, 0]]
    assert 1 == robot_in_grid.count_move(arr, 3, 3)

    arr = [[0, 0, -1],[0,0,0], [0, -1, 0], [0, 0, 0]]
    assert 3 == robot_in_grid.count_move(arr, 4, 3)