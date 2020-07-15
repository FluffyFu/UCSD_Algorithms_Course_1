from different_summands import optimal_summands


def test_optimal_summands():
    n = 6
    assert optimal_summands(n) == [1, 2, 3]

    n = 8
    assert optimal_summands(n) == [1, 2, 5]

    n = 2
    assert optimal_summands(n) == [2]
