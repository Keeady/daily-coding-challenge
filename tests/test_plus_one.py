from Array import plus_one


def test_plus_one():
    arr = [9, 9]
    assert [1,0,0] == plus_one.plus_one(arr)

    arr = [1,2,3]
    assert [1,2,4] == plus_one.plus_one(arr)

    arr = [4,3,2,1]
    assert [4,3,2,2] == plus_one.plus_one(arr)