# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10


def fibonacci_sum(n):
    """
    Using the general formula of F(n), we can prove:
        sum_{i=0}_{n} F(i) = F(n+1) + F(n) - 1

    We already know the last digit of F(n) has periodicity. Using the result from the
    5-th homework, we know the periodicity for mode 10 is 60. So the results become:
        last_digit(F((n+1) % 60)) + last_digit(F(n % 60)) - 1
    """
    s = n % 60

    previous = 0
    current = 1

    for _ in range(s):
        previous, current = current, (previous + current)

    return (previous + current - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
