from fractional_knapsack import get_optimal_value
import pytest


def test_fractional_knapsack():
    capacity = 50
    weights = [20, 50, 30]
    values = [60, 100, 120]

    assert get_optimal_value(capacity, weights, values) == pytest.approx(180)

    capacity = 10
    weights = [30, ]
    values = [500, ]
    assert get_optimal_value(
        capacity, weights, values) == pytest.approx(166.6667)

