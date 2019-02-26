from Array import count_steps


def test_count():
    assert 1 == count_steps.count_opt(0)
    assert 1 == count_steps.count_opt(1)
    assert 2 == count_steps.count_opt(2)
    assert 4 == count_steps.count_opt(3)
    assert 13 == count_steps.count_opt(5)
    assert 7 == count_steps.count_opt(4)

    assert 1 == count_steps.top_down(0)
    assert 1 == count_steps.top_down(1)
    assert 2 == count_steps.top_down(2)
    assert 4 == count_steps.top_down(3)
    assert 13 == count_steps.top_down(5)
    assert 7 == count_steps.top_down(4)