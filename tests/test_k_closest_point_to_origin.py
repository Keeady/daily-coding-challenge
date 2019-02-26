from Array import k_closest_point_to_origin


def test_k_closest():

    points = [[1, 3], [-2, 2]]
    K = 1
    assert [[-2,2]] == k_closest_point_to_origin.find_k_closest_points(points, K)

    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    assert [[3, 3], [-2, 4]] == k_closest_point_to_origin.find_k_closest_points(points, K)

    points = [[3, 3], [5, -1], [-2, 4]]
    K = 1
    assert [[3, 3]] == k_closest_point_to_origin.find_k_closest_points(points, K)

    points = [[6, 10], [-3, 3], [-2, 5], [0, 2]]
    K = 3
    assert [[-3, 3], [0, 2], [-2, 5]] == k_closest_point_to_origin.find_k_closest_points(points, K)

    points = [[6, 10], [-3, 3], [-2, 5], [0, 2]]
    K = 2
    assert [[0, 2], [-3, 3]] == k_closest_point_to_origin.find_k_closest_points(points, K)

    points = [[-173, 399], [62, -213], [71, 282], [-45, 851], [710, 982], [493, 985], [-529, -946], [-83, 78], [624, -785],
     [877, -351], [500, -376], [-601, -305], [-23, -79], [-82, 906], [-143, 500], [-249, -260], [10, 706], [-904, -632],
     [-402, 458], [303, -970], [93, -552], [-362, -743], [705, 986], [900, -524], [-680, -204], [-726, 890],
     [-138, 742], [-76, 714], [813, 474], [443, 23], [-422, 117], [768, 214], [863, 562], [728, -204], [778, 147],
     [-56, -751], [240, 454], [-106, -701], [-897, -770], [572, 433], [-658, 97], [-301, -466], [902, -371],
     [-38, -662], [-872, 191], [659, 294], [852, 965], [-37, 665], [541, -920], [-537, 704]]
    K = 20

    result = [[-23,-79],[-83,78],[62,-213],[71,282],[-249,-260],[-173,399],[-422,117],[443,23],[240,454],[-143,500],[-301,-466],[93,-552],[-402,458],[500,-376],[-38,-662],[-658,97],[-37,665],[-601,-305],[10,706],[-106,-701]]

    res = k_closest_point_to_origin.find_k_closest_points(points, K)

    missing = []
    for r in result:
        if r not in res:
            print(r)
            missing.append(r)

    if len(missing) > 0:
        assert False

