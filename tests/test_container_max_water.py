from Array import container_max_water


def test_container_max_water():
    arr = [1,8,6,2,5,4,8,3,7]
    assert 49 == container_max_water.find_container_max_water(arr)
    assert 4 == container_max_water.find_container_max_water([1,1,1,1,1])
    assert 1 == container_max_water.find_container_max_water([1, 1])
    assert 2 == container_max_water.find_container_max_water([1, 2, 1])
    assert 1 == container_max_water.find_container_max_water([1, 2])
    assert 18048 == container_max_water.find_container_max_water([76,155,15,188,180,154,84,34,187,142,22,5,27,183,111,128,50,58,2,112,179,2,100,111,115,76,134,120,118,103,31,146,58,198,134,38,104,170,25,92,112,199,49,140,135,160,20,185,171,23,98,150,177,198,61,92,26,147,164,144,51,196,42,109,194,177,100,99,99,125,143,12,76,192,152,11,152,124,197,123,147,95,73,124,45,86,168,24,34,133,120,85,81,163,146,75,92,198,126,191])


def test_container_most_water():
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    assert 49 == container_max_water.find_container_most_water(arr)
    assert 4 == container_max_water.find_container_most_water([1, 1, 1, 1, 1])
    assert 1 == container_max_water.find_container_most_water([1, 1])
    assert 2 == container_max_water.find_container_most_water([1, 2, 1])
    assert 1 == container_max_water.find_container_most_water([1, 2])
    assert 18048 == container_max_water.find_container_most_water(
        [76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100, 111, 115,
         76, 134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135, 160, 20, 185, 171,
         23, 98, 150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100, 99, 99, 125, 143, 12, 76,
         192, 152, 11, 152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133, 120, 85, 81, 163, 146, 75, 92,
         198, 126, 191])

