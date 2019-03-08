from Array import three_sums


def test_3_sums():
    assert [[-1, 0, 1],[-1, -1, 2]] == three_sums.sums([-1, 0, 1, 2, -1, -4])