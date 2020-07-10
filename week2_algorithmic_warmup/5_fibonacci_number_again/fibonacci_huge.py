# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge(n, m):
    data = [0, 1]  # store mode results

    previous = 0
    current = 1

    flag = False  # indicates if a period is reached.
    for _ in range(n-1):
        previous, current = current, previous + current
        data.append(current % m)
        T = int(len(data) / 2)
        if check_period(data, T):
            flag = True
            break
    if flag:
        # already reached periodicity
        index = n % T
        return data[index]
    else:
        return data[-1]


def check_period(data, T):
    """
    Check if the serial data has a periodicity T start from the first element
    of data.

    This is not a general method. Because there is no way to definitively conclude
    there is a periodicity is data is finite.

    Args:
        data (list): a list of int.

        T (int): periodicity to check.

    Return
        bool.
    """
    if len(data) < 2 * T:
        # not enough data to decide.
        return False
    for i in range(T):
        if data[i] != data[i + T]:
            return False
    return True


if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
