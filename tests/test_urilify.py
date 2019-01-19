from String import urlify


def test_urilify():
    str = 'Mr John Smith    '
    l = 13

    assert urlify.urlify(str, l) == 'Mr%20John%20Smith'

    str = 'Mr John is Smith      '
    l = 16

    assert urlify.urlify(str, l) == 'Mr%20John%20is%20Smith'

