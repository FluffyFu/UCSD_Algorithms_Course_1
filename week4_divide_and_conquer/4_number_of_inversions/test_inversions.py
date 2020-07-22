from inversions import merge_and_count, get_number_of_inversions, get_number_of_inversions_naive
from hypothesis import given, settings, assume
from hypothesis import strategies


def test_merge_and_count():
    a = [1, 2, 10, 3, 4, 5]
    b = [0] * len(a)
    l1, r1 = 0, 2
    l2, r2 = 3, 5

    n_inversions = merge_and_count(a, b, l1, r1, l2, r2)
    assert n_inversions == 3
    assert a == [1, 2, 3, 4, 5, 10]


def test_get_number_of_inversions_naive():
    a = [1, 2, 10, 3, 4, 5]
    n_inversions = get_number_of_inversions_naive(a)
    assert n_inversions == 3

    a = [1]
    n_inversions = get_number_of_inversions_naive(a)
    assert n_inversions == 0

    a = [3, 2, 1]
    n_inversions = get_number_of_inversions_naive(a)
    assert n_inversions == 3


@given(a=strategies.lists(strategies.integers(min_value=1, max_value=int(1E9))))
@settings(max_examples=100)
def test_get_number_of_inversions(a):
    assume(len(a) > 0)
    a_copy = list(a)
    b = [0] * len(a)

    left, right = 0, len(a) - 1
    assert get_number_of_inversions(
        a, b, left, right) == get_number_of_inversions_naive(a_copy)

