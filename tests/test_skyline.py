from Array import skyline


def test_skyline():
    arr = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

    assert [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]] == skyline.calc_skyline(arr)
    assert [[2,10],[12,0],[15,10],[24,0]] == skyline.calc_skyline([[2,9,10],[3,7,10],[5,12,10],[15,20,10],[19,24,10]])

    assert [[0,0],[0,0]] == skyline.calc_skyline([[0,0,0]])

    #assert [[2,20],[9,0]] == skyline.calc_skyline([[2,9,10],[2,9,14],[2,9,16],[2,9,18],[2,9,20]])

    assert [[2,15],[7,10],[9,0]] == skyline.calc_skyline([[2,9,10],[2,7,15]])
