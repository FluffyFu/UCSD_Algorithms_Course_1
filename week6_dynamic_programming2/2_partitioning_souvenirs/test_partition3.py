from partition3 import subset_sum
import pudb


def test_subset_sum():
    # pudb.set_trace()
    S = [9, 8, 3, 7, 2, 1]
    assert subset_sum(S, len(S)-1, 10, 10, 10) == 1

    S = [4, 1, 4, 3]
    assert subset_sum(S, len(S)-1, 4, 4, 4) == 1
