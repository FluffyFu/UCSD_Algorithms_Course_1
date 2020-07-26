from sorting import partition3, randomized_quick_sort_2, randomized_quick_sort
from hypothesis import given, settings, assume
from hypothesis import strategies
import pytest


def test_partition3():
    a = [2, 2, 3, 1]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (1, 2)
    assert a[0] == 1
    assert a[1:3] == [2, 2]
    assert a[3] == 3

    a = [2, 2, 2, 1]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (1, 3)
    assert a[0] == 1
    assert a[1:] == [2, 2, 2]

    a = [2, 2, 3, 2]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (0, 2)
    assert a[-1] == 3

    a = [2]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (0, 0)

    a = [2, 3, 9, 2, 9]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (0, 1)
    assert a[:2] == [2, 2]

    a = [9, 3, 9, 2, 2]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (3, 4)
    assert a[3:] == [9, 9]


@given(a=strategies.lists(strategies.integers(min_value=1, max_value=int(1E8))))
@settings(max_examples=100)
def test_randomized_quick_sort_random(a):
    assume(len(a) > 0)
    l, r = 0, len(a) - 1
    a_copy = list(a)
    assert randomized_quick_sort_2(
        a, l, r) == randomized_quick_sort(a_copy, l, r)


@pytest.mark.repeat(30)
def test_randomized_quick_sort():
    a = [2, 3, 9, 2, 9]
    randomized_quick_sort(a, 0, len(a)-1)
    assert a == [2, 2, 3, 9, 9]
