# Uses python3

import sys


def lcs2(a, b):
    """
    Find the longest common subsequence of two sequences.

    For example,
        a = [2, 7, 5], b = [2, 5], result = 2, where (2, 5) is the longest common sequences

        a = [2, 7, 8, 3], b = [5, 2, 8, 7], result = 2, where(2, 7) or (2, 8) is the longest common sequences.

    Args:
        a (list of int)

        b (list of int)

    Returns:
        int, the length of the longest common subsequence.
    """
    n_a = len(a)
    n_b = len(b)

    # D[i][j] represent the LCS of a[:i] and b[:j]
    D = [[0] * (n_b+1) for _ in range(n_a+1)]

    for i in range(1, n_a+1):
        for j in range(1, n_b+1):
            if a[i-1] == b[j-1]:
                D[i][j] = D[i-1][j-1]+1
            else:
                D[i][j] = max((D[i][j-1], D[i-1][j]))

    return D[n_a][n_b]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
