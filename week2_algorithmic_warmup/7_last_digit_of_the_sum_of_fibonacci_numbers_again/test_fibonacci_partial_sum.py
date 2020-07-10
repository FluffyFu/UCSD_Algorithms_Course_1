from fibonacci_partial_sum import fibonacci_partial_sum_naive, fibonacci_partial_sum
from hypothesis import given, settings, assume
import hypothesis.strategies as st


@given(m=st.integers(min_value=0, max_value=int(1E3)), n=st.integers(min_value=0, max_value=int(1E3)))
@settings(max_examples=100)
def test_fibonacci_partial_sum(n, m):
    assume(n >= m)
    assert fibonacci_partial_sum_naive(m, n) == fibonacci_partial_sum(m, n)

