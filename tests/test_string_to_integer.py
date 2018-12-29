from String import string_to_integer

def test_str_to_integer():
    str = "123"
    assert string_to_integer.string_to_integer(str) == 123

def test_str_to_integer_neg():
    str = "-123"
    assert string_to_integer.string_to_integer(str) == -123

def test_str_to_integer_long():
    str = "1230123"
    assert string_to_integer.string_to_integer(str) == 1230123