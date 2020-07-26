from majority_element import get_majority_element, get_majority_element_naive
from hypothesis import given, settings, assume
from hypothesis import strategies


@given(a=strategies.lists(strategies.integers(min_value=1, max_value=int(1E9))))
@settings(max_examples=100)
def test_get_marjority_element_random(a):
    assume(len(a) > 0)
    left = 0
    right = len(a) - 1
    a_copy = list(a)
    assert get_majority_element(
        a_copy, left, right) == get_majority_element_naive(a, left, right)


def test_get_marjority_element():
    a = [512766168, 717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772]
    assert get_majority_element_naive(a, 0, 9) == 0
    assert get_majority_element(a, 0, 9) == 0
