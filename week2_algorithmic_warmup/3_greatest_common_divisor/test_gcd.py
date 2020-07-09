from gcd import gcd_naive, gcd
from hypothesis import given, assume, settings
import hypothesis.strategies as st

@given(a=st.integers(min_value=1, max_value=int(10E5)), b=st.integers(min_value=1, max_value=int(10E5)))
@settings(max_examples=200)
def test_gcd(a, b):
    assume((a > 0) and (b > 0))
    assert gcd(a, b) == gcd_naive(a, b)

def test_gcd_case():
    assert gcd(int(2*10E9), int(2*10E8)) == int(2*10E8)
