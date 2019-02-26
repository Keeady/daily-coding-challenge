from String import fizzbuzz


def test_fizzbuzz():
    assert [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz'] == fizzbuzz.print_fizz_buzz(1, 10)
    assert ['buzz', 11, 'fizz', 13, 14, 'fizzbuzz'] == fizzbuzz.print_fizz_buzz(10, 16)

def test_fizzbuzz():
    assert [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz'] == fizzbuzz.print_fizz_buzz_no_module(1, 10)
    assert ['buzz', 11, 'fizz', 13, 14, 'fizzbuzz'] == fizzbuzz.print_fizz_buzz_no_module(10, 16)
