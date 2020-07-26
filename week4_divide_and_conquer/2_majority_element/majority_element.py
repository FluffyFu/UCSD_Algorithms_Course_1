# Uses python3
import sys
from collections import Counter


def get_majority_element(a, left, right):
    _, c = helper(a, left, right)

    if c > 0:
        return 1
    else:
        return 0


def helper(a, left, right):
    """
    Find the majority element and its counts in the given array.

    Args:
        a (list of int)

        left (int): left end of the window.

        right (int): right end of the window.

    Returns:
        (int, int), the majority element and its counts. If there's no majority
        element, returns (-1, 0)
    """
    if (left > right):
        return -1, 0
    if (left == right):
        return a[left], 1

    mid = left + int((right - left)/2)

    m1, c1 = helper(a, left, mid)
    m2, c2 = helper(a, mid+1, right)

    if (c1 == 0 and c2 == 0):
        return -1, 0

    if c1 > 0:
        # majority exits in the first half, check if it's the global majority.
        for i in range(mid+1, right + 1):
            if a[i] == m1:
                c1 += 1

    if c2 > 0:
        # majority exits in the second half, check if it's the global majority.
        for i in range(left, mid+1):
            if a[i] == m2:
                c2 += 1

    if c1 >= int((right - left + 1)/2) + 1:
        return m1, c1

    if c2 >= int((right - left + 1)/2) + 1:
        return m2, c2

    return -1, 0


def get_majority_element_naive(a, left, right):
    c = Counter(a)
    _, counts = c.most_common(1)[0]
    if len(a) == 1 and counts == 1:
        return 1
    elif counts >= int(len(a)/2) + 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a, 0, n-1))
