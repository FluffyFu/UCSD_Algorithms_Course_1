from points_and_segments import binary_search, fast_count_segments, naive_count_segments,\
    fast_count_segments_2
from hypothesis import given, settings, assume
from hypothesis import strategies
import numpy as np
import pytest


@pytest.fixture
def sorted_array():
    min_val = int(-1E8)
    max_val = int(1E8)
    n = 50000
    return sorted(np.random.randint(low=min_val, high=max_val, size=n))


def test_binary_search():
    array = [1, 5, 8, 9]
    l = 0
    r = len(array) - 1

    p = 2
    assert binary_search(array, p, l, r, 'left') == 1

    p = 5
    assert binary_search(array, p, l, r, 'left') == 1

    p = 5
    assert binary_search(array, p, l, r, 'right') == 2

    p = 0
    assert binary_search(array, p, l, r, 'right') == 0

    p = 10
    assert binary_search(array, p, l, r, 'right') == 4

    array = [0]
    l = 0
    r = len(array) - 1
    p = 0
    assert binary_search(array, p, l,  r, 'right') == 1

    p = 0
    assert binary_search(array, p, l,  r, 'left') == 0

    p = -1
    assert binary_search(array, p, l,  r, 'right') == 0

    p = 1
    assert binary_search(array, p, l, r, 'right') == 1


@given(a=strategies.lists(strategies.integers(min_value=-int(1E3), max_value=int(1E3))),
       pts=strategies.lists(strategies.integers(min_value=-int(1E3), max_value=int(1E3))))
@settings(max_examples=20)
def test_fast_count_segments(a, pts):
    assume(len(a) >= 2 and len(a) % 2 == 0)
    a = sorted(a)

    pts = list(set(pts))

    starts = [a[i] for i in range(0, len(a), 2)]
    ends = [a[i] for i in range(1, len(a), 2)]

    assert fast_count_segments(
        starts, ends, pts) == naive_count_segments(starts, ends, pts)


@given(a=strategies.lists(strategies.integers(min_value=-int(1E3), max_value=int(1E3))),
       pts=strategies.lists(strategies.integers(min_value=-int(1E3), max_value=int(1E3))))
@settings(max_examples=20)
def test_fast_count_segments_2(a, pts):
    assume(len(a) >= 2 and len(a) % 2 == 0)
    a = sorted(a)

    pts = list(set(pts))

    starts = [a[i] for i in range(0, len(a), 2)]
    ends = [a[i] for i in range(1, len(a), 2)]

    assert fast_count_segments_2(
        starts, ends, pts) == fast_count_segments(starts, ends, pts)


def test_fast_count_segments_time():
    starts = [1, 2, 3, 4]
    ends = [5, 5, 5, 5]
    points = [2, 3, 5, 5]

    assert fast_count_segments(starts, ends, points) == [2, 3, 4, 4]

    starts = [2, 4, 4]
    ends = [3, 5, 5]
    points = [5, 5, 5]

    assert fast_count_segments(starts, ends, points) == [2, 2, 2]


@pytest.mark.repeat(10)
def test_fast_count_segments_stress():
    # takes about 8 seconds for 10 reps.
    k = 5000
    n = int(1E4)
    starts = [-1] * n
    ends = [n] * n
    points = np.random.randint(low=0, high=n, size=k)
    fast_count_segments(starts, ends, points)
