from Number import roman_to_int

def test_roman_to_int():
    num = 'MCMXCIV'
    assert 1994 == roman_to_int.convert_roman_to_int(num)

    num = 'XXVII'
    assert 27 == roman_to_int.convert_roman_to_int(num)

    num = 'LVIII'
    assert 58 == roman_to_int.convert_roman_to_int(num)

    num = 'MDCCCXC'
    assert 1890 == roman_to_int.convert_roman_to_int(num)