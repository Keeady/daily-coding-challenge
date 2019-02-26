from Array import optimal_combination_sum


def test_optimal_comb():
    assert [[1000, 2000], [2000, 1000]] == optimal_combination_sum.find_optimal_combination([1000, 2000],[1000, 1500, 2000], 3000)
    assert [[5000, 5000], [7000, 3000]] == optimal_combination_sum.find_optimal_combination([3000, 5000,7000,10000],[2000, 3000, 4000, 5000], 10000)

    #assert [[1, 3], [2, 1]] == optimal_combination_sum.find_combination_sum([[1,1000], [2,2000]],[[1,1000], [2,1500], [3,2000]], 3000)
    #assert [[2, 4], [3, 2]] == optimal_combination_sum.find_combination_sum([[1,3000], [2,5000], [3,7000], [4,10000]],[[1,2000], [2,3000], [3,4000], [4,5000]],10000)