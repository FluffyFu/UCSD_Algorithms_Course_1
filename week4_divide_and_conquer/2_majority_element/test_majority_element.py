from majority_element import get_majority_element, get_majority_element_naive
from hypothesis import given, settings, assume
from hypothesis import strategies


@given(a=strategies.lists(strategies.integers(min_value=1, max_value=int(1E9))))
@settings(max_examples=100)
def test_get_marjority_element(a):
    assume(len(a) > 0)
    left = 0
    right = len(a) - 1
    assert get_majority_element(
        a, left, right) == get_majority_element_naive(a, left, right)
