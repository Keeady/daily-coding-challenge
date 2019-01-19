from Number import is_palindrome


def test_is_palindrome():
    num = 123
    assert False == is_palindrome.is_palindrome(num)

    num = 121
    assert True == is_palindrome.is_palindrome(num)

    num = 12021
    assert True == is_palindrome.is_palindrome(num)


def test_is_palindrome_2():
    num = 123
    #assert False == is_palindrome.is_palindrome_int(num)

    num = 121
    #assert True == is_palindrome.is_palindrome_int(num)

    num = 1221
    #assert True == is_palindrome.is_palindrome_int(num)

    num = 12
    assert False == is_palindrome.is_palindrome_int(num)

    num = 120345643021
    assert False == is_palindrome.is_palindrome_int(num)