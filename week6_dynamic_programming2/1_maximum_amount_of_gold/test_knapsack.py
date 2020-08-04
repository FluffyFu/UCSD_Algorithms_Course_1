from knapsack import optimal_weight
import pudb


def test_optimal_weight():
    # pudb.set_trace()
    W = 10
    w = [1, 4, 8]
    assert optimal_weight(W, w) == 9

    W = 4
    w = [1, 2, 3]
    assert optimal_weight(W, w) == 4

    W = 4
    w = [2, 2, 3]
    assert optimal_weight(W, w) == 4

    W = 1
    w = [2]
    assert optimal_weight(W, w) == 0

