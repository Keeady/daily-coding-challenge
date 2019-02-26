from Array import combination_sum, combination_sum_2


def test_comb():
    arr = [2,5,3]

    assert [[2, 2, 3], [2, 5]] == combination_sum_2.calc_comb(arr, 7)
    arr = [2, 5, 3, 4]

    assert [[2, 2, 3], [2, 5], [3, 4]] == combination_sum_2.calc_comb(arr, 7)