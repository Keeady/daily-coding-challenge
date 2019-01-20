from Array import search_insert_position


def test_search_insert_position():
    arr = [1,3,5,6]
    value = 5
    assert 2 == search_insert_position.search_insert_position(arr, value)

    arr = [1, 3, 5, 6]
    value = 4
    assert 2 == search_insert_position.search_insert_position(arr, value)

    assert 1 == search_insert_position.search_insert_position([1,3,5,6], 2)

    assert 4 == search_insert_position.search_insert_position([1,3,5,6], 7)

    assert 0 == search_insert_position.search_insert_position([1,3,5,6], 0)