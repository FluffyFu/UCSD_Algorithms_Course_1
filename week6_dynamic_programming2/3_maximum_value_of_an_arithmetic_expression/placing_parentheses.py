# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    """
    Given an arithmetic expression which contains addition, subtraction and multiplication. Find
    the maximum value by changing the computation order.

    Args:
        dataset (str): arithmetic string. For example, 5-8+7*4-8+9. It only contains single digits,
        i.e. 0 - 9.

    Returns:
        int, the maximum value obtained from the expression.
    """
    digits, operations = extract_digits_and_operations(dataset)
    n_digits = len(digits)

    # D[i][j] represents the maximum value using a[i], a[i+1] ... a[j]
    # and operations[i], operations[i+1] ... operations[j-1] (if j-1 < i, there is only
    # a single digit, no operation is used.)
    D = [[None for _ in range(n_digits)] for _ in range(n_digits)]

    for i in range(n_digits):
        D[i][i] = digits[i]

    # d[i][j] represents the minimum values
    d = [[None for _ in range(n_digits)] for _ in range(n_digits)]
    for i in range(n_digits):
        d[i][i] = digits[i]

    # fill the matrix from the diag
    for delta in range(1, n_digits):
        for i in range(0, n_digits-delta):
            j = i + delta
            d[i][j], D[i][j] = min_max_sub_value(i, j, D, d, operations)

    return D[0][n_digits-1]


def min_max_sub_value(i, j, D, d, operations):
    """
    Find the minimum value for subproblem from the i-th digit to j-th digit.
    """
    min_result = 10000000
    max_result = -10000000

    for k in range(i, j):
        op = operations[k]
        min_first = d[i][k]
        max_first = D[i][k]
        min_second = d[k+1][j]
        max_second = D[k+1][j]

        c1 = evalt(min_first, min_second, op)
        c2 = evalt(min_first, max_second, op)
        c3 = evalt(max_first, min_second, op)
        c4 = evalt(max_first, max_second, op)

        max_c = max((c1, c2, c3, c4))
        min_c = min((c1, c2, c3, c4))

        if max_c > max_result:
            max_result = max_c

        if min_c < min_result:
            min_result = min_c

    return min_result, max_result


def extract_digits_and_operations(dataset):
    """
    Helper function to extract digits and operations from the given arithmetic string.

    Args:
        dataset (str): arithmetic string. For example, 5-8+7*4-8+9. It only contains single digits,
        i.e. 0 - 9.

    Returns:
        a list of int and a list of strings.
    """
    op_set = {'+', '-', '*'}
    digits = []
    operations = []
    for s in dataset:
        if s in op_set:
            operations.append(s)
        else:
            digits.append(int(s))

    return digits, operations


if __name__ == "__main__":
    print(get_maximum_value(input()))
