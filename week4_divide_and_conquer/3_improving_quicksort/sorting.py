# Uses python3
import sys
import random


def partition3(a, l, r):
    """
    Partition the given array into three parts with respect to the first element.

    i.e. x < pivot, x == pivot and x > pivot

    Args:
        a (list)

        l (int): the left index of the array.

        r (int): the right index of the array.

    Returns:
        lt(int), gt(int), s.t. a[0, lt-1] < pivot, a[lt, gt] == pivot and a[gt+1, :] > pivot

        We don't need to worry about lt-1 and gt+1 are out of bound, because they'll be taken
        care of by the recursion base case.
    """
    x = a[l]
    lt = l
    gt = r

    i = l + 1

    while i <= gt:
        if a[i] < x:
            lt += 1
            a[lt], a[i] = a[i], a[lt]
            i += 1
        elif a[i] == x:
            i += 1
        elif a[i] > x:
            # i should not be incremented here, because the switch moves
            # unseen element to i.
            a[gt], a[i] = a[i], a[gt]
            gt -= 1

    a[l], a[lt] = a[lt], a[l]
    return lt, gt


def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort_2(a, l, r):
    """
    Use two partitions to perform quick sort.
    """
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def randomized_quick_sort(a, l, r):
    """
    Use three partitions to perform quick sort.
    """
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    lt, gt = partition3(a, l, r)
    randomized_quick_sort(a, l, lt-1)
    randomized_quick_sort(a, gt+1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
