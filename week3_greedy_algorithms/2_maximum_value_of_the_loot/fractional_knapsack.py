# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    """
    Find the optimal value that can be stored in the knapsack.

    Args:
        capacity (int): the capacity of the knapsack.

        weights (list): a list of item weights.

        values (list): a list of item values. The order matches weight input.

    Returns:
        float, optimal value.
    """
    v_per_w = [(value / weight, index)
               for index, (value, weight) in enumerate(zip(values, weights))]

    sorted_v_per_w = sorted(v_per_w, key=lambda x: x[0])[::-1]

    v = 0
    for avg_v, index in sorted_v_per_w:
        if capacity <= 0:
            break
        w = min(capacity, weights[index])
        capacity -= w
        v += avg_v * w

    return round(v, 4)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
