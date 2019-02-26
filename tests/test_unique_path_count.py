from Matrix import unique_path


def test_unique_path():
    assert 3 == unique_path.count_unique_path(3, 2)
    assert 28 == unique_path.count_unique_path(7, 3)
    assert 0 == unique_path.count_unique_path(0, 0)
    assert 1 == unique_path.count_unique_path(1, 1)
    assert 1 == unique_path.count_unique_path(1, 2)
    assert 1 == unique_path.count_unique_path(2, 1)
    assert 924 == unique_path.count_unique_path(7, 7)
