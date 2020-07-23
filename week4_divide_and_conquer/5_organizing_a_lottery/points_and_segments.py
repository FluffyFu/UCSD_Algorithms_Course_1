# Uses python3
import sys
from collections import Counter
import numpy as np

import time


def fast_count_segments(starts, ends, points):
    """
    Given a list of line segments, specified by starts and ends, and a list of points,
    for each point, find how many line segments covers it.

    We first sort the points and for each segment, we check its start and end w.r.t
    the sorted array. In this way, we know the points that's covered by this segment.

    In fact, the most difficult part to make this program fast enough is how to store
    the counts of each point. If we use a simple loop, in the worst case, the running time
    is O(n*2). Here, I kinda cheat using a numpy array to make it faster.

    The lesson learnt here is when designing an algorithm, we not only need to consider the time used
    to calculate the results, but also the time to store them.

    Args:
        starts (list): a list of start of line segments.

        ends (list): a list of end of line segments.

        points (list): list of integers.

    Returns:
        a list, same length as points, each element represents the number of times that
        element is covered.
    """
    n = len(points)
    cnt = [0] * n
    # create a map between the index of the original and sorted element
    sorted_pts_map = sorted(
        [(pt, i) for i, pt in enumerate(points)], key=lambda x: x[0])

    np_cnt = np.zeros(n)
    sorted_pts = [x[0] for x in sorted_pts_map]

    for s, e in zip(starts, ends):
        l1 = binary_search(sorted_pts, s, 0, n-1, 'left')
        l2 = binary_search(sorted_pts, e, 0, n-1, 'right')
        # python list is not fast enough to do this operation.
        np_cnt[l1:l2] += 1

    # map the counts to the original index.
    for key, val in enumerate(np_cnt):
        index = sorted_pts_map[key][1]
        cnt[index] = int(val)
    return cnt


def fast_count_segments_2(starts, ends, points):
    """
    For each point, check how many segments intersect with it. This method avoid the
    storage issue mentioned in the previous function.

    The idea is for a point p, check how many ends is greater or equal to it, denote by a.
    Then, check how many starts is greater than p, denote by b. The result is a - b. (From the symmetry
    perspective, you can also check how many starts is smaller or equal to q, and subtract those with
    end smaller than p.)

    It's easy to understand a is a superset A of the result (segments that contains p). There are two
    mutually exclusive subsets that in A: one with its start smaller or equal to p (S), the other is its
    start greater than p (G). S is the result set.

    The key point is that to determine the size of G, we don't need to know the relation between starts,
    and ends, only the values of starts is enough. This is because end >= start always holds, if start > p,
    ends must > p. So every start found this way belong to G.

    The bonus of doing things this way actually reveals what binary_search('left'/'right') really does.
    It calculates the number of elements smaller or equal than p ('right'), and smaller than p ('left').
    """
    starts = sorted(starts)
    ends = sorted(ends)
    n = len(starts)

    cnt = [0] * len(points)

    for i, p in enumerate(points):

        # (n - lx) is size of S
        lx = binary_search(starts, p, 0, n-1, 'right')
        # (n - ly) is size of A
        ly = binary_search(ends, p, 0, n-1, 'left')

        # (n - ly) - (n - lx)
        cnt[i] = lx - ly

    return cnt


def binary_search(array, p, l, r, side):
    """
    Search p in the subset, specified by [l, r], of the given ordered array.

    See docstring of fast_count_segments_2 about what the function really is.

    If p is not found, returns the correct position where it should be inserted.

    If
        p is found, side == 'left', return the index of the first found element.

        p is found, side == 'right', return the index of first element that is larger than p.

    If we follow this convention
        binary_search(end) - binary_search(start) always returns the correct number of points
        this is covered by [start, end] segment.

    Args:
        array (list): ordered int.

        p (int): number need to be searched.

        l (int): left boundary of the array subset.

        r (int): right boundary of the array subset.

        side (str): 'left' or 'right', choose to return the left most or right most element if
            the element contains duplicates.

    Returns:
        int
    """
    # base case
    if l == r:
        if array[l] < p:    # not found, but larger
            return l + 1
        elif array[l] > p:  # not found, but smaller
            return l
        elif side == 'left':  # found, return the first p
            return l
        else:               # found, return the first not p.
            return l + 1

    # standard binary search except the recursive call when p is found
    while (l <= r):
        mid = l + (r - l) // 2
        if array[mid] == p:
            if side == 'left':
                # note mid instead of mid - 1 is used, otherwise,
                # the first p will be missed.
                return binary_search(array, p, l, mid, side)
            elif side == 'right':
                return binary_search(array, p, mid+1, r, side)
        elif array[mid] > p:
            r = mid - 1
        else:
            l = mid + 1
    return l


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
