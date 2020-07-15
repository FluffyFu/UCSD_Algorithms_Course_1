# Uses python3
import sys


def get_change(m):
    """
    Find the minimum number of coins needed to change the input value into coins with
    denominations 1, 5, and 10.

    m (int): money value.

    Returns:
        int, number of coins needed to make the change.
    """
    n_10, r = divmod(m, 10)
    n_5, r = divmod(r, 5)
    n_2, r = divmod(r, 1)

    return n_10 + n_5 + n_2


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
