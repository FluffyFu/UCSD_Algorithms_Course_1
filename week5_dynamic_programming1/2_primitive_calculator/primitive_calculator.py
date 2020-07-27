# Uses python3
import sys


def optimal_sequence(n):
    MAX = 1000000
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    elif n == 3:
        return [1, 3]

    # tracking[i] stores the i's previous number, tracking[0] is empty
    tracking = [0] * (n+1)
    tracking[1] = 1  # 1 is always on the list.
    tracking[2] = 1  # 2 comes from 1 by multiplying 2.
    tracking[3] = 1  # 3 comes from 1 by multiplying 3.
    # dp[i] stores the minimum number of operations to get i, dp[0] is invalid
    dp = [-1, 0, 1, 1]

    for i in range(4, n+1):

        c1 = dp[i-1]  # add one operation.

        if i % 2 == 0:  # multiply 2 operation.
            c2 = dp[i//2]
        else:
            c2 = MAX

        if i % 3 == 0:  # multiply 3 operation
            c3 = dp[i//3]
        else:
            c3 = MAX

        min_operation = min([c1, c2, c3])
        dp.append(min_operation + 1)

        if min_operation == c1:
            tracking[i] = i-1
        elif min_operation == c2:
            tracking[i] = i // 2
        else:
            tracking[i] = i // 3

    sequence = []
    current = n
    while current > 1:
        sequence.append(current)
        current = tracking[current]

    sequence.append(1)

    return sequence[::-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')
