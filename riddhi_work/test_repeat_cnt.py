import repeat_cnt


def test_repeat():
    response = repeat_cnt.repeat([1, 2 , 'riddhipatel', 22, 33, 22, 22])
    assert response == {22: 3, 'd': 2, 'i': 2, 'a': 1, 1: 1, 2: 1, 'e': 1, 33: 1, 'h': 1, 'l': 1, 'p': 1, 'r': 1, 't': 1}

    response1 = repeat_cnt.repeat(123)
    assert response1 == "User input should be a list type, not a number."
