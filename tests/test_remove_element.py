from Array import remove_element


def test_remove_element():
    arr = [1, 1, 3, 2]
    assert 3 == remove_element.remove_element(arr, 3)
    assert arr[0:3] == [1, 1, 2]

    arr = [1, 2, 2, 1, 3, 4, 3, 5]
    assert 6 == remove_element.remove_element(arr, 3)
    assert arr[0:6] == [1, 2, 2, 1, 4, 5]