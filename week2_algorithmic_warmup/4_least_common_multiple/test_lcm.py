from lcm import lcm_naive, lcm
from hypothesis import given, settings
import hypothesis.strategies as st

@given(a=st.integers(min_value=1, max_value=int(10E2)), b=st.integers(min_value=1, max_value=int(10E3)))
@settings(max_examples=10)
def test_lcm(a, b):
    assert lcm_naive(a, b) == lcm(a, b)

def test_lcm_cases():
    a = 1022
    b = 4331
    assert lcm(a, b) == lcm_naive(a, b)

    a = 701
    b = 6479
    assert lcm(a, b) == lcm_naive(a, b)
