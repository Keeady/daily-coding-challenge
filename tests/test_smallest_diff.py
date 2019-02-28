from Array import smallest_difference


def test_pos_arrs():
    assert 3 == smallest_difference.find_smallest_diff([1,3,15,11,2],[23,127,235,19,8])

    assert 2 == smallest_difference.find_smallest_diff([5],[7])

    assert 1 == smallest_difference.find_smallest_diff([-5,-3,-14],[-7,-9,-6])

    assert 2 == smallest_difference.find_smallest_diff([1,3,15,11,2,-3],[23,127,235,19,8,-5])


