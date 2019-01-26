from Array import merge_sorted_array


def test_merge_2_arrays():
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]

    assert [1,2,2,3,5,6] == merge_sorted_array.merge_sorted_array(arr1, 3, arr2, 3)


def test_min_max_arrays():
    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [4, 5, 6]

    assert [1, 2, 3, 4, 5, 6] == merge_sorted_array.merge_sorted_array(arr1, 3, arr2, 3)


def test_max_min_arrays():
    arr1 = [4, 5, 6, 0, 0, 0]
    arr2 = [1, 2, 3]

    assert [1, 2, 3, 4, 5, 6] == merge_sorted_array.merge_sorted_array(arr1, 3, arr2, 3)


def test_eq_arrays():
    arr1 = [4, 5, 6, 0, 0, 0]
    arr2 = [4, 5, 6]

    assert [4, 4, 5, 5, 6, 6] == merge_sorted_array.merge_sorted_array(arr1, 3, arr2, 3)


def test_empty_arrays():
    arr1 = []
    arr2 = []

    assert [] == merge_sorted_array.merge_sorted_array(arr1, 0, arr2, 0)


def test_right_zero_arrays():
    arr1 = [1, 2, 3, 4, 5, 6]
    arr2 = []

    assert [1, 2, 3, 4, 5, 6] == merge_sorted_array.merge_sorted_array(arr1, 6, arr2, 0)


def test_left_zero_arrays():
    arr2 = [1, 2, 3, 4, 5, 6]
    arr1 = [0, 0, 0, 0, 0, 0]

    assert [1, 2, 3, 4, 5, 6] == merge_sorted_array.merge_sorted_array(arr1, 0, arr2, 6)


def test_mixed_arrays():
    arr1 = [4, 7, 11, 15, 16, 20, 0]
    arr2 = [59]

    assert [4, 7, 11, 15, 16, 20, 59] == merge_sorted_array.merge_sorted_array(arr1, 6, arr2, 1)

    arr2 = [4, 7, 11, 15, 16, 20]
    arr1 = [59, 0, 0, 0, 0, 0, 0]

    assert [4, 7, 11, 15, 16, 20, 59] == merge_sorted_array.merge_sorted_array(arr1, 1, arr2, 6)