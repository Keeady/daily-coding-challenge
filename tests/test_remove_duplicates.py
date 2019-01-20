from Array import remove_duplicates


def test_remove_duplicates():
    arr = [2, 2, 2, 3, 4]
    assert 3 == remove_duplicates.remove_duplicates(arr)
    assert arr[0:3] == [2, 3, 4]

def test_remove_dup():
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert 5 == remove_duplicates.remove_duplicates(arr)
    assert arr[0:5] == [0, 1, 2, 3, 4]