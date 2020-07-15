from change import get_change


def test_get_change():
    assert get_change(2) == 2
    assert get_change(28) == 6
