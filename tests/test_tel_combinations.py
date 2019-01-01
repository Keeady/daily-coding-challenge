from String import telephone_combination, telephone_util

def test_gen_tel_comb():
    tel = [9,1,9,4,4,2,6]
    tel_comb = telephone_combination.telephone_number(telephone_util.telephone_util(), tel)
    words = tel_comb.print_words()
    assert len(words) == 729

def test_gen_tel_comb2():
    tel = [9,9,9,9,9,9,9]
    tel_comb = telephone_combination.telephone_number(telephone_util.telephone_util(), tel)
    words = tel_comb.print_words()
    assert len(words) == pow(3, 7)

def test_clean():
    tel = [4, 9, 7, 1, 9, 2, 7]
    tel_comb = telephone_combination.telephone_number(telephone_util.telephone_util(), tel)
    words = tel_comb.print_words()
    assert len(words) == 729

def test_clean_ones():
    tel = [1, 1, 1, 1, 1, 1, 1]
    tel_comb = telephone_combination.telephone_number(telephone_util.telephone_util(), tel)
    words = tel_comb.print_words()
    assert len(words) == 1

def test_clean_ones_two():
    tel = [1, 1, 2, 1, 1, 1, 1]
    tel_comb = telephone_combination.telephone_number(telephone_util.telephone_util(), tel)
    words = tel_comb.print_words()
    assert len(words) == 3

def test_clean_ones_twos():
    tel = [1, 1, 2, 1, 3, 1, 1]
    tel_comb = telephone_combination.telephone_number(telephone_util.telephone_util(), tel)
    words = tel_comb.print_words()
    assert len(words) == 9