from String import combination_string


def test_gen_lspaces():
    str = '   '
    combination = combination_string.Combination(str)
    c = combination.find_combination()
    assert len(c) == 0

def test_gen_l0():
    str = ''
    combination = combination_string.Combination(str)
    c = combination.find_combination()
    assert len(c) == 0

def test_gen_l1():
    str = 'w'
    combination = combination_string.Combination(str)
    c = combination.find_combination()
    assert len(c) == 1
    assert c == ['w']

def test_gen_l2():
    str = 'wx'
    combination = combination_string.Combination(str)
    c = combination.find_combination()
    assert len(c) == 3
    assert c == ['x', 'xw', 'w']

def test_gen_l3():
    str = 'wxy'
    combination = combination_string.Combination(str)
    c = combination.find_combination()
    assert len(c) == 7
    assert c == ['y', 'yx', 'x', 'yw', 'yxw', 'xw', 'w']

def test_gen_l4():
    str = 'wxyz'
    combination = combination_string.Combination(str)
    c = combination.find_combination()
    assert len(c) == 15
    assert c == ['z', 'zy', 'y', 'zx', 'zyx', 'yx', 'x', 'zw', 'zyw', 'yw', 'zxw', 'zyxw', 'yxw', 'xw', 'w']