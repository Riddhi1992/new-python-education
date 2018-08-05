# from rough import div
#
#
# def test_div():
#     response = div(100, 2000)
#     assert response[0] == 182
#     assert response != [0]

import rough


def test_prime():
    response = rough.rough(500, 10000)
    assert response[0] == 503
    assert response[2] != 503

    response2 = rough.rough('sssdfafaf', 100)
    assert response2 == 'The value is suppose to be positive number not string'

    response3 = rough.rough(-100, -100000)
    assert response3 == 'The value is suppose to be positive, no negative value allowed'

