from Number import reverse_integer


def test_reverse_int():
    assert 321 == reverse_integer.reverse_integer(123)
    assert -321 == reverse_integer.reverse_integer(-123)

def test_reverse_int2():
    #assert 321 == reverse_integer.reverse_int(123)
    assert -321 == reverse_integer.reverse_int(-123)