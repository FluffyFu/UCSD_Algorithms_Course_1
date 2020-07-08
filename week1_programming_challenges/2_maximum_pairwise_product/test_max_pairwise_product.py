from max_pairwise_product import max_pairwise_product
import numpy as np
from hypothesis import given, assume
import hypothesis.strategies as st


def test_max_pairwise_product_stress():
    size = int(10E5)
    low = 2
    high = int(2*10E5)

    test_times = 2
    for _ in range(test_times):
        numbers = np.random.randint(low=low, high=high, size=size)
        ordered_numbers = sorted(numbers)

        truth = ordered_numbers[-1] * ordered_numbers[-2]
        result = max_pairwise_product(numbers)

        assert truth == result, 'result: {}, truth: {}\n numbers: {}'.format(
            result, truth, ordered_numbers)

@given(st.lists(st.integers(min_value=2, max_value=int(2*10E5))))
def test_max_pairwise_product_property(numbers):
    assume(len(numbers) > 1)
    result = max_pairwise_product(numbers)

    ordered_numbers = sorted(numbers)
    assert result == ordered_numbers[-2] * ordered_numbers[-1]
