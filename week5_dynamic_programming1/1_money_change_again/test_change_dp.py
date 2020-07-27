from change_dp import get_change


def test_get_chagen():

    m = 1
    assert get_change(m) == 1

    m = 2
    assert get_change(m) == 2

    m = 3
    assert get_change(m) == 1

    m = 4
    assert get_change(m) == 1

    m = 34
    assert get_change(m) == 9

    m = 16
    assert get_change(m) == 4
