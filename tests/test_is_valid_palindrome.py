from String import isValidPalindrome

def test_isvalid():
    s = "A man, a plan, a canal: Panama"
    assert True == isValidPalindrome.isValid(s)

def test_is_not_valid():
    s = "race a car"
    assert False == isValidPalindrome.isValid(s)