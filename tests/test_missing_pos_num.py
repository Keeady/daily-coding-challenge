from Array import find_missing_positive_num


def test_missing_num():
    arr = [1,2,0]
    assert 3 == find_missing_positive_num.find_missing_pos_num(arr)
    assert 1 == find_missing_positive_num.find_missing_pos_num([7,8,9,11,12])
    assert 2 == find_missing_positive_num.find_missing_pos_num([3,4,-1,1])
    assert 1 == find_missing_positive_num.find_missing_pos_num([])
    assert 2 == find_missing_positive_num.find_missing_pos_num([1])
    assert 1 == find_missing_positive_num.find_missing_pos_num([5])
    assert 1 == find_missing_positive_num.find_missing_pos_num([-1,-2,-3,-4,-5,-6])
    assert 7 == find_missing_positive_num.find_missing_pos_num([1,2,3,4,5,6])
    assert 5 == find_missing_positive_num.find_missing_pos_num([-1,1,-2,2,-3,3,-4,4])
    assert 2 == find_missing_positive_num.find_missing_pos_num([1,1000])