import pudb
from lcs3 import lcs3


def test_lcs_3():
    a = [1, 2, 3]
    b = [2, 1, 3]
    c = [1, 3, 5]

    assert lcs3(a, b, c) == 2

    a = [8, 3, 2, 1, 7]
    b = [8, 2, 1, 3, 8, 10, 7]
    c = [6, 8, 3, 1, 4, 7]

    assert lcs3(a, b, c) == 3
