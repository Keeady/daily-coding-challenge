from String import tel_combination_clean

def test_clean():
    tel = [4, 9, 7, 1, 9, 2, 7]
    output = [4, 9, 7, 1, 9, 2, 7]
    words = tel_combination_clean.gen_tel_combination(tel, 0, [], output)
    assert len(words) == 729

def test_clean_full():
    tel = [4, 9, 7, 3, 9, 2, 7]
    output = [4, 9, 7, 3, 9, 2, 7]
    words = tel_combination_clean.gen_tel_combination(tel, 0, [], output)
    assert len(words) == pow(3, 7)

def test_clean_ones():
    tel = [1, 1, 1, 1, 1, 1, 1]
    output = [1, 1, 1, 1, 1, 1, 1]
    words = tel_combination_clean.gen_tel_combination(tel, 0, [], output)
    assert len(words) == 1

def test_clean_ones_two():
    tel = [1, 1, 2, 1, 1, 1, 1]
    output = [1, 1, 2, 1, 1, 1, 1]
    words = tel_combination_clean.gen_tel_combination(tel, 0, [], output)
    assert len(words) == 3

def test_clean_ones_twos():
    tel = [1, 1, 2, 1, 3, 1, 1]
    output = [1, 1, 2, 1, 1, 1, 1]
    words = tel_combination_clean.gen_tel_combination(tel, 0, [], output)
    assert len(words) == 9