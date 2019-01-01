from String import permutation_string


def test_gen_l1():
    str = 'o'
    p = permutation_string.perm_rec(str)


    assert len(p) == 1
    assert p == ['o']

def test_gen_l2():
    str = 'ox'
    p = permutation_string.perm_rec(str)

    assert len(p) == 2
    assert p == ['ox', 'xo']

def test_gen_l3():
    str = 'hat'
    p = permutation_string.perm_rec(str)
    assert len(p) == 6
    assert p == ['hat', 'aht', 'ath', 'hta', 'tha', 'tah']

    p = permutation_string.perm_rec('aaa')
    assert len(p) == 6
    assert p == ['aaa', 'aaa', 'aaa', 'aaa', 'aaa', 'aaa']

def test_gen_l4():
    str = 'hats'
    p = permutation_string.perm_rec(str)
    assert len(p) == 24


def test_gen_l5():
    str = 'haste'
    p = permutation_string.perm_rec(str)
    assert len(p) == 120

