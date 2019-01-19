from String import is_palindrome_permutation

def test_is_palindrome_permutation():
    str = 'Tact Coa'

    assert True == is_palindrome_permutation.is_palindrome_permutation(str)

    str = 'Tact oCoa'

    assert True == is_palindrome_permutation.is_palindrome_permutation(str)

    str = 'Tact Ca'

    assert True == is_palindrome_permutation.is_palindrome_permutation(str)\

    str = 'Duck Duck Go'

    assert False == is_palindrome_permutation.is_palindrome_permutation(str)

    str = 'tactcoapapa'

    assert True == is_palindrome_permutation.is_palindrome_permutation(str)