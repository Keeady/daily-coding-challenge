from String import first_occurence_substr


def test_find_first_occurrence():
    str = 'hello'
    needle = 'll'
    assert 2 == first_occurence_substr.find_first_occurrence_substr(str, needle)

    haystack = "aaaaa"
    needle = "bba"
    assert -1 == first_occurence_substr.find_first_occurrence_substr(str, needle)

    str = 'q'
    needle = 'q'
    assert 0 == first_occurence_substr.find_first_occurrence_substr(str, needle)
