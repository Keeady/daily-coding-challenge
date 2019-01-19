from String import one_away


def test_one_away():
    str = 'pale'
    str2 = 'ple'

    assert True == one_away.one_away(str2, str)

    str = 'pale'
    str2 = 'bake'

    assert False == one_away.one_away(str2, str)

    str = 'pales'
    str2 = 'pale'

    assert True == one_away.one_away(str2, str)

    str = 'pale'
    str2 = 'bale'

    assert True == one_away.one_away(str2, str)

    str = 'pale'
    str2 = 'mask'

    assert False == one_away.one_away(str2, str)