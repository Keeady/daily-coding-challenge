from String import is_permutation

def test_is_permutation():
    str1 = 'abc'
    str2 = 'cba'

    assert is_permutation.is_permutation(str1, str2) == True

    str1 = 'aBce'
    str2 = 'eCba'

    assert is_permutation.is_permutation(str1, str2) == True

    str1 = 'abcde'
    str2 = 'ecba'

    assert is_permutation.is_permutation(str1, str2) == False