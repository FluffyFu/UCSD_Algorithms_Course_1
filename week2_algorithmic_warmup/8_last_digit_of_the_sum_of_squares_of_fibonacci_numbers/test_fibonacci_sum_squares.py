from fibonacci_sum_squares import fibonacci_sum_squares_naive, fibonacci_sum_squares
from hypothesis import given, settings
import hypothesis.strategies as st


@given(n=st.integers(min_value=0, max_value=1000))
@settings(max_examples=100)
def test_fibonacci_sum_squares(n):
    assert fibonacci_sum_squares_naive(n) == fibonacci_sum_squares(n)
