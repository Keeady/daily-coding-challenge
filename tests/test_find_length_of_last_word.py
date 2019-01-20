from String import length_of_last_word


def test_length_of_last_word():
    input = 'hello world'
    assert 5 == length_of_last_word.find_length_of_last_word(input)

    input = 'hello world '
    assert 5 == length_of_last_word.find_length_of_last_word(input)