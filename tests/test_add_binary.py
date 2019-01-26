from String import add_binary


def test_add_binary():
    sum = 0
    sum += 1 - '0'

    assert '1001' == add_binary.add_binary('101', '100')