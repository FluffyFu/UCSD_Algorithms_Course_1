# Uses python3

import sys
from functools import cmp_to_key


def largest_number_naive(a):
    """
    Compose the largest number out of a set of positive integers.

    Computational time: n**2

    Args:
        a (a list of str): a list of positive integers, each element is between [1, 1000]

    Returns:
        str, the largest number composed from the given integers.
    """
    res = ""
    copy_a = a[:]
    while copy_a:
        max_digit = '0'
        for digit in copy_a:
            if is_greater(digit, max_digit) > 0:
                max_digit = digit
        res += max_digit
        copy_a.remove(max_digit)

    return res


def largest_number(a):
    """
    Compose the largest number out of a set of positive integers.

    Computational time (n*log(n))

    Args:
        a (a list of str): a list of positive integers, each element is between [1, 1000]

    Returns:
        str, the largest number composed from the given integers.
    """
    sorted_a = sorted(a, key=cmp_to_key(is_greater), reverse=True)
    return "".join(sorted_a)


def is_greater(s1, s2):
    """
    Helper function for largest_number_naive.

    Special comparison function between two string.

    Args:
        s1 (str)

        s2 (str)

    Returns:
        1: concatenate(s1, s2) > concatenate(s2, s1)
        0: concatenate(s1, s2) == concatenate(s2, s1)
        -1: concatenate(s1, s2) < concatenate(s2, s1)
    """
    a1 = s1 + s2
    a2 = s2 + s1

    if a1 > a2:
        return 1
    elif a1 < a2:
        return -1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
