
from fibonacci import calc_fib, calc_fib_naive


def test_calc_fib():
    min_n = 0
    max_n = 40

    for n in range(min_n, max_n):
        assert calc_fib(n) == calc_fib_naive(n)
