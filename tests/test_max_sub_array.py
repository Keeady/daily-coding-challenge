from Array import max_sub_array


def test_find_max_sub_array():
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert 6 == max_sub_array.find_max_sub_array(arr)

    arr = [-1, 1, 3, 2, -3, 1, 2]
    assert 6 == max_sub_array.find_max_sub_array(arr)

    arr = [4, -2, -1, 2, 1, 3]
    assert 7 == max_sub_array.find_max_sub_array(arr)

    arr = [-1, -2]
    assert -1 == max_sub_array.find_max_sub_array(arr)