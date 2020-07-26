from closest import x_within_distance, minimum_distance, naive_minimum_distance
from hypothesis import given, settings, assume
from hypothesis import strategies
import pytest


def test_x_within_distance():
    pts = [(-2, 0), (-1, 0), (0, 0), (2, 0), (2, 0), (5, 0)]
    l = 0
    r = len(pts) - 1

    ref = 0
    d = 1.2
    assert x_within_distance(pts, l, r, ref, d) == (1, 2)

    ref = 0
    d = 1
    assert x_within_distance(pts, l, r, ref, d) == (2, 2)

    ref = 0
    d = 3
    assert x_within_distance(pts, l, r, ref, d) == (0, 4)


def test_minimum_distance():
    x = [0, 0, 0]
    y = [0, 1, -1]

    assert minimum_distance(x, y) == pytest.approx(1.0)


@given(strategies.lists(strategies.tuples(strategies.integers(min_value=int(-1E9), max_value=int(1E9)),
                                          strategies.integers(min_value=int(1E-9), max_value=int(1E9)))))
@settings(max_examples=100)
def test_minimum_distance_random(pts):
    assume(len(pts) >= 2)
    x = [i[0] for i in pts]
    y = [i[1] for i in pts]
    assert minimum_distance(x, y) == pytest.approx(
        naive_minimum_distance(x, y), rel=1E-4)

