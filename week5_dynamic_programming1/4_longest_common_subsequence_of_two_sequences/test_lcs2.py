from lcs2 import lcs2
import pudb


def test_lcs2():
    a = [7]
    b = [1, 2, 3, 4]
    assert lcs2(a, b) == 0

    # pudb.set_trace()
    a = [2, 7, 5]
    b = [2, 5]
    assert lcs2(a, b) == 2

    a = [2, 7, 8, 3]
    b = [5, 2, 8, 7]
    assert lcs2(a, b) == 2

