# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10


def fibonacci_partial_sum(from_, to):
    """
    Calculate the last digit of partial sum of Fibonacci numbers:
        sum_{i=m}^{i=n}(F(i))
    Following the results from the 6-th homework, this equals to the last digit of

        (F((n+1) % 60) + F(n % 60) - 1) - (F(m % 60) + F((m-1) % 60) - 1)
    """
    if from_ == 0:
        return fibonacci_last_digit_base_10(to)

    digit_n = fibonacci_last_digit_base_10(to)
    digit_m = fibonacci_last_digit_base_10(from_ - 1)

    return (10 + digit_n - digit_m) % 10  # 10 is added to make sure positive.


def fibonacci_last_digit_base_10(n):
    """
    Returns the last digit of F(n)
    """
    s = n % 60
    previous = 0
    current = 1

    for _ in range(s):
        previous, current = current, (previous + current)

    return (previous + current - 1) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))

