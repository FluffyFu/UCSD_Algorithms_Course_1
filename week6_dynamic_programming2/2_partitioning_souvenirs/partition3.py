# Uses python3
import sys
import itertools


def partition3(A):
    """
    Check if the element in A can be partitioned into 3 parts whose sum are equal.

    Args:
        List of int.

    Returns:
        0 or 1, 0 means impossible, 1 means possible.
    """

    if len(A) < 3:
        return False

    # convert to 0 and 1
    return int((sum(A) % 3) == 0 and subset_sum(A, len(A)-1, sum(A)/3, sum(A)/3, sum(A)/3))


def subset_sum(S, n, a, b, c):
    """
    Given an array S of integers (index from 0 to n are available). Check if it is possible to
    use elements in S to form sums of a, b and c without repetition.

    Args:
        S (list of int): candidates.

        n (int): the maximum index of S that can be used.

        a (int): first target.

        b (int): second target.

        c (int): third target.

    Returns:
        bool.

    """

    if a == 0 and b == 0 and c == 0:
        return True

    if n < 0:
        return False

    if a - S[n] >= 0:
        A = subset_sum(S, n-1, a-S[n], b, c)
        if A:
            return True

    if b - S[n] >= 0:
        B = subset_sum(S, n-1, a, b-S[n], c)
        if B:
            return True

    if c - S[n] >= 0:
        C = subset_sum(S, n-1, a, b, c-S[n])
        if C:
            return True

    return False


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

