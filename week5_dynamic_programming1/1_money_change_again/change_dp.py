# Uses python3
import sys


def get_change(m):
    """
    Given a positive integer, find the minimum number of coins to change the
    number with denominations of 1, 3, 4

    Args:
        m (int): m > 1

    Returns:
        int, minimum number of coins to change the money.
    """
    a = [1, 2, 1, 1]  # a[i] stores the minimum number of ways to change i+1.

    for i in range(4, m):
        a.append(min(a[i-1], a[i-3], a[i-4]) + 1)

    return a[m-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
