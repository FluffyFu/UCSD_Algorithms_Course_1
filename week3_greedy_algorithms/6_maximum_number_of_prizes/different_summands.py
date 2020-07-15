# Uses python3
import sys


def optimal_summands(n):
    """
    Given a positive integer n, find the maximum number of pair-wise-different numbers
    such that their sum is n.

    Args:
        n (int)

    Returns:
        a list of integers.
    """
    summands = []
    i = 1
    rest = n

    while 2 * i < rest:
        summands.append(i)
        rest -= i
        i += 1

    summands.append(rest)
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
