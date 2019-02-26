from Matrix import min_path_sum


def test_calc_min_sum():
    m = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

    assert 7 == min_path_sum.calc_min_path_sum(m)