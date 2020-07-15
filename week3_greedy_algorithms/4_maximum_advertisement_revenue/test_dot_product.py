from dot_product import max_dot_product


def test_max_dot_product():
    a = [23]
    b = [39]
    assert max_dot_product(a, b) == 897

    a = [1, 3, -5]
    b = [-2, 4, 1]
    assert max_dot_product(a, b) == 23
