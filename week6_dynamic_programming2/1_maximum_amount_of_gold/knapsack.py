# Uses python3
import sys


def optimal_weight(W, w):
    """
    Finite knapsack problem. Given the knapsack capacity W and a list of gold bricks
    weight w, find the maximum weight of gold that could fit into the knapsack.

    Args:
        W (int): knapsack total capacity.

        w (list of int): a list of gold brick weights.

    Returns:
        int, the maximum weight that could fit into the knapsack.
    """
    n = len(w)

    # D[i][j] represents the maximum weight that could be fit in a knapsack
    # with capacity j using w0, w2 ... wi.
    D = [[0 for _ in range(W+1)] for _ in range(n)]

    # fill the first row, i.e. only using w1 to fill knapsack from 1 to W.
    for j in range(1, W+1):
        if j < w[0]:
            D[0][j] = 0
        else:
            D[0][j] = w[0]

    # fill in matrix D row by row.
    for i in range(1, n):
        for j in range(1, W+1):
            current_w = w[i]

            # case 1: contains w[i], the result reduce to fill
            # in knapsack of capacity W - w[i], with w0, w1, .. wi-1
            if j - current_w < 0:
                s1 = -1
            elif j == current_w:
                s1 = current_w
            else:
                s1 = D[i-1][j-current_w] + current_w

            # case 2: does not contains w[i]
            s2 = D[i-1][j]

            D[i][j] = max(s1, s2)

    return D[n-1][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
