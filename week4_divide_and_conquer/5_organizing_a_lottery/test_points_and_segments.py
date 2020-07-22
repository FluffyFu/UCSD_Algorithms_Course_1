from points_and_segments import binary_search, single_line_cross, fast_count_segments, naive_count_segments
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
    p = 2
    assert binary_search(array, p, 'left') == (False, 1)

    p = 5
    assert binary_search(array, p, 'left') == (True, 1)

    p = 5
    assert binary_search(array, p, 'right') == (True, 1)

    p = 0
    assert binary_search(array, p, 'right') == (False, 0)

    p = 10
    assert binary_search(array, p, 'right') == (False, 4)

    array = [0]

    p = 0
    assert binary_search(array, p, 'right') == (True, 0)

    p = -1
    assert binary_search(array, p, 'right') == (False, 0)

    p = 1
    assert binary_search(array, p, 'right') == (False, 1)


@pytest.mark.repeat(50)
def test_binary_search_stress(sorted_array):
    p = int(1E8)
    binary_search(sorted_array, p, 'right')


def test_single_line_corss():
    array = [1, 5, 5, 8, 9]

    start, end = 0, 2
    assert single_line_cross(array, start, end) == (0, 1)

    start, end = 0, 6
    assert single_line_cross(array, start, end) == (0, 3)

    start, end = 1, 6
    assert single_line_cross(array, start, end) == (0, 3)

    start, end = 2, 6
    assert single_line_cross(array, start, end) == (1, 3)

    start, end = 0, 10
    assert single_line_cross(array, start, end) == (0, 5)

    start, end = 5, 8
    assert single_line_cross(array, start, end) == (1, 4)

    array = [0]
    start, end = 0, 0
    assert single_line_cross(array, start, end) == (0, 1)


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


@pytest.fixture
def np_array():
    n = 50000
    a = np.random.randint(low=0, high=500, size=50000)
    return a


@pytest.fixture
def np_index():
    index = [i for i in range(1, 20000)]
    return index


@pytest.mark.repeat(1000)
def test_numpy_indexing_speed(np_array, np_index):
    np_array[np_index] += 1


@pytest.fixture
def py_list():
    n = int(1E5)
    return [0] * n


@pytest.mark.repeat(1000)
def test_loop_operation_speed(py_list):
    n = int(1E5)
    for i in range(n):
        py_list[i] += 1


@pytest.mark.repeat(1000)
def test_iterator_operation_speed(py_list):
    # about 20 % faster than a for loop.
    n = int(1E5)
    py_list[0:n] = map((1).__add__, py_list[0:n])
