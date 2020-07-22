# Uses python3
import sys
from collections import Counter
import numpy as np

import time


def fast_count_segments(starts, ends, points):
    """
    Given a list of line segments, specified by starts and ends, and a list of points,
    for each point, find how many line segments covers it.

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
    cnt = [0] * len(points)
    # create a map between the index of the original and sorted element
    sorted_pts_map = sorted(
        [(pt, i) for i, pt in enumerate(points)], key=lambda x: x[0])

    np_cnt = np.zeros(len(points))
    sorted_pts = [x[0] for x in sorted_pts_map]

    for s, e in zip(starts, ends):
        l1, l2 = single_line_cross(sorted_pts, s, e)
        # python list is not fast enough to do this operation.
        np_cnt[l1:l2] += 1

    for key, val in enumerate(np_cnt):
        index = sorted_pts_map[key][1]
        cnt[index] = int(val)
    return cnt


def binary_search(array, p, side):
    """
    Search p in the given ordered array.

    If found, returns True and its left most or right most index (in case of duplicates).
    If not found, returns False and the index it should be inserted.

    Args:
        array (list): ordered int.

        p (int): number need to be searched.

        side (str): 'left' or 'right', choose to return the left most or right most element if
            the element contains duplicates.

    Returns:
        bool, int
    """
    l = 0
    r = len(array) - 1

    while(l <= r):
        mid = l + (r - l) // 2
        if array[mid] == p:
            if side == 'left':
                # find the left most index
                sub_l = 0
                sub_r = mid
                while (sub_l <= sub_r):
                    sub_mid = sub_l + (sub_r - sub_l) // 2
                    if array[sub_mid] == p:
                        sub_r = sub_mid - 1
                    else:
                        sub_l = sub_mid + 1
                return True, sub_l

            elif side == 'right':
                # find the right most index
                sub_l = mid
                sub_r = r
                while (sub_l <= sub_r):
                    sub_mid = sub_l + (sub_r - sub_l) // 2
                    if array[sub_mid] == p:
                        sub_l = sub_mid + 1
                    else:
                        sub_r = sub_mid - 1
                return True, sub_r
        elif array[mid] > p:
            r = mid - 1
        else:
            l = mid + 1

    return False, l


def single_line_cross(array, start, end):
    """
    Given a sorted array and a line segment, find the index range [l1, l2) that is
    covered by the segment.

    Args:
        array (list): a list of ordered int.

        start (int): start of the line segment (inclusive).

        end (int): end of the line segment (inclusive).

    Returns:
        a tuple of index, the second is not inclusive.
    """
    b1, l1 = binary_search(array, start, 'left')
    b2, l2 = binary_search(array, end, 'right')

    if b1 and b2:
        return l1, l2+1
    elif not b1 and not b2:
        return l1, l2
    elif b1 and not b2:
        return l1, l2
    else:
        return l1, l2+1


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
