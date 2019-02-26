from String import rotate_string_ntimes


def test_rotate():
    assert '' == rotate_string_ntimes.rotate('', 10)
    assert 'a' == rotate_string_ntimes.rotate('a', 10)
    assert 'abcdefgh' == rotate_string_ntimes.rotate('abcdefgh', 8)
    assert 'defghabc' == rotate_string_ntimes.rotate('abcdefgh', 3)
    assert 'fghabcde' == rotate_string_ntimes.rotate('abcdefgh', 13)

    assert '' == rotate_string_ntimes.smart_rotate('', 10)
    assert 'a' == rotate_string_ntimes.smart_rotate('a', 10)
    assert 'abcdefgh' == rotate_string_ntimes.smart_rotate('abcdefgh', 8)
    assert 'defghabc' == rotate_string_ntimes.smart_rotate('abcdefgh', 3)
    assert 'fghabcde' == rotate_string_ntimes.smart_rotate('abcdefgh', 13)
    assert rotate_string_ntimes.rotate('abcdefgh', 100) == rotate_string_ntimes.smart_rotate('abcdefgh', 100)