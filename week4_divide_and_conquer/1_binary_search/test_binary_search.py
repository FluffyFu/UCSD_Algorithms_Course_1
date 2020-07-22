from binary_search import binary_search, linear_search
from hypothesis import given, settings, assume
import hypothesis.strategies as st


@given(a=st.lists(st.integers()), b=st.integers())
@settings(max_examples=1000)
def test_binary_search(a, b):
    assume(len(a) > 0)
    a = sorted(a)
    assert binary_search(a, b) == linear_search(a, b)
