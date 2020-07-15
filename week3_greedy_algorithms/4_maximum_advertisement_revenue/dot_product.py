# Uses python3

import sys


def max_dot_product(a, b):
    """
    Given two list of numbers a, b. Find the optimal value of:
        sum_{i} (a_i * c_i)
    where c is a permutation of  b.

    Args:
        a (list of int)

        b (list of int):

    Returns:
        int.
    """
    a = sorted(a)
    b = sorted(b)

    return sum([i * j for i, j in zip(a, b)])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

