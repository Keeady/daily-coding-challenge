from Array import min_combination_waste
import sys

def test_comb_waste():
    arr = [200, 100, 30]
    qty = 182
    min_waste = sys.maxsize

    waste = min_combination_waste.find_min_waste(arr, qty, min_waste)
    assert waste == 8

def test_min_comb_waste():
    arr = [200, 150, 100, 70, 50, 30]
    qty = 182
    min_waste = sys.maxsize

    waste = min_combination_waste.find_min_waste(arr, qty, min_waste)
    assert waste == 8

def test_min_comb_waste2():
    arr = [200, 150, 100, 70, 50, 30, 5]
    qty = 182
    min_waste = sys.maxsize

    waste = min_combination_waste.find_min_waste(arr, qty, min_waste)
    assert waste == 3