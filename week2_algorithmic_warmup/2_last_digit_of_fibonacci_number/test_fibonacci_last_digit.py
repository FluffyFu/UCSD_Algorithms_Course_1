import numpy as np
from fibonacci_last_digit import get_fibonacci_last_digit_naive, get_fibonacci_last_digit


def test_fibonacci_last_digit():
    n_min = 0
    n_max = int(10E4)
    n = 2000

    for n in np.random.randint(low=n_min, high=n_max, size=n):
        assert get_fibonacci_last_digit(n) == get_fibonacci_last_digit_naive(n)

def test_fibonacci_last_digit_cases():
    assert get_fibonacci_last_digit(327305) == 5
    assert get_fibonacci_last_digit(3) == 2
    assert get_fibonacci_last_digit(331) == 9
