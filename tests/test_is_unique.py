from String import is_unique

def test_is_unique():
    str = 'excuse moi'
    assert is_unique.is_unique(str) == False

    str = 'excus moi'
    assert is_unique.is_unique(str) == True

    str = 'e'
    assert is_unique.is_unique(str) == True

    str = 'EXCUSe moi'
    assert is_unique.is_unique(str) == False


def test_is_unique_sort():
    str = 'excuse moi'
    assert is_unique.is_unique_sort(str) == False

    str = 'excus moi'
    assert is_unique.is_unique_sort(str) == True

    str = 'e'
    assert is_unique.is_unique_sort(str) == True

    str = 'EXCUSe moi'
    assert is_unique.is_unique_sort(str) == False