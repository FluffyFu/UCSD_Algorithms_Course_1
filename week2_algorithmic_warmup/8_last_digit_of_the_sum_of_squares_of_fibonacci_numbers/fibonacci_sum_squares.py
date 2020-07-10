# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares(n):
    """
    Calculate the last digit of F(0)^2 + F(1)^2 + ... + F(n)^2

    Think the square as the area of a square. And from the geometry, we have the sum is
    equal to:
        F(n) * (F(n) + F(n-1))
    We know the last digit of F(n) has periodicity of 60. Using this fact, the last digit can
    be calculated easily.
    """
    if n % 60 == 0:
        return 0

    n = n % 60
    previous = 0
    current = 1

    for _ in range(n-1):
        previous, current = current, (previous + current) % 10

    return (current * (previous + current)) % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares(n))
