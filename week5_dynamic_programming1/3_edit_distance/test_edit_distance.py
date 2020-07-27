from edit_distance import edit_distance
import pudb


def test_edit_distance():
    s = 'ab'
    t = 'ab'
    assert edit_distance(s, t) == 0

    # pudb.set_trace()
    s = 'ab'
    t = 'ac'
    assert edit_distance(s, t) == 1

    s = 'short'
    t = 'ports'
    assert edit_distance(s, t) == 3

    s = 'editing'
    t = 'distance'
    assert edit_distance(s, t) == 5
