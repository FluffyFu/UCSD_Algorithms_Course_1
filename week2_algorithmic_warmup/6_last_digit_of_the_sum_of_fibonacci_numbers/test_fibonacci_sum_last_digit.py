from fibonacci_sum_last_digit import fibonacci_sum_naive, fibonacci_sum
import hypothesis.strategies as st
from hypothesis import given, settings


@given(st.integers(min_value=0, max_value=int(1E5)))
@settings(max_examples=100)
def test_fibonacci_sum_last_digit(n):
    assert fibonacci_sum_naive(n) == fibonacci_sum(n)
