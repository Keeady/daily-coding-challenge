from Array import find_element_in_sorted_array

def test_find_ele_in_sorted_array():
    arr = []
    el = 1
    assert find_element_in_sorted_array.find_element(arr, el) == -1

    arr = [1,2,3,4,5,7,7,8,9,10]
    el = 1
    assert find_element_in_sorted_array.find_element(arr, el) == 0

    el = 10
    assert find_element_in_sorted_array.find_element(arr, el) == 9


    el = 5
    assert find_element_in_sorted_array.find_element(arr, el) == 4

    el = 8
    assert find_element_in_sorted_array.find_element(arr, el) == 7

    el = 3
    assert find_element_in_sorted_array.find_element(arr, el) == 2

    el = 6
    assert find_element_in_sorted_array.find_element(arr, el) == -1
