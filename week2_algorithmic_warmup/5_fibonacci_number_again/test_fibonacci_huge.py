from fibonacci_huge import get_fibonacci_huge, get_fibonacci_huge_naive
from hypothesis import given
import hypothesis.strategies as st


@given(n=st.integers(min_value=1, max_value=int(10E4)), m=st.integers(min_value=2, max_value=1000))
def test_get_fibonacci_huge(n, m):
    assert get_fibonacci_huge(n, m) == get_fibonacci_huge_naive(n, m)

def test_get_fibonacci_huge_cases():
    n = 2816213588
    m = 239
    assert get_fibonacci_huge(n, m) == 151
