# Uses python3

import sys


def lcs3(a, b, c):
    """
    Find the length of a longest common subsequence of three sequences.

    Args:
        a (list of int)

        b (list of int)

        c (list of int)

    Returns:
        int
    """
    n_a = len(a)
    n_b = len(b)
    n_c = len(c)

    # D[i][j][k] represents the LCS for a[:i], b[:j], c[:k]
    D = [[[0] * (n_c + 1) for _ in range(n_b + 1)] for _ in range(n_a + 1)]

    for i in range(1, n_a+1):
        for j in range(1, n_b+1):
            for k in range(1, n_c+1):
                if a[i-1] == b[j-1] == c[k-1]:
                    D[i][j][k] = D[i-1][j-1][k-1] + 1
                else:
                    D[i][j][k] = max(
                        (D[i-1][j][k], D[i][j-1][k], D[i][j][k-1]))
    return D[n_a][n_b][n_c]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[: an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[: bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[: cn]
    print(lcs3(a, b, c))
