from divisible_7_13 import div

def test_div():
    response = div(324, 444372)
    response[0] == 364

    response2 = div(-25, -1)
    assert response2 == "the value must be postive"
