from prime import prim
def test_prime():
    response = prim(500, 10000)
    response[0] == [503]

    response2 = prim(-1, 200)
    assert response2 == "the value must be postive"
