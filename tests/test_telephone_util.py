from String import telephone_util

def test_util():
    k = 2
    p = 1

    util = telephone_util.telephone_util()
    assert util.get_char_key(k, p) == 'a'

def test_util_0():
    k = 0
    p = 1

    util = telephone_util.telephone_util()
    assert util.get_char_key(k, p) == ''
