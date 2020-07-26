# Uses python3
import sys
import math

MAX_DISTANCE = 10 ** 18


def minimum_distance(x, y):
    pts = sorted([(i, j) for i, j in zip(x, y)], key=lambda x: x[0])
    l = 0
    r = len(pts) - 1

    return min_dist(pts, l, r)


def naive_minimum_distance(x, y):
    n = len(x)

    min_d = MAX_DISTANCE
    for i in range(n):
        for j in range(i+1, n):
            d = math.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)
            if d < min_d:
                min_d = d

    return min_d


def min_dist(pts, l, r):
    """
    Given a list of sorted points (by x coordinate) and the range [l, r],
    find the minimum distance among the points.

    Args:
        pts (list of tuples): [(x1, y1), (x2, y2), ..(xn, yn)], sorted by x.

        l (int): left boundary index.

        r (int): right boundary index.

    Returns:
        float.
    """
    if r - l == 1:
        # two elements in the array.
        return distance(pts[l], pts[r])
    elif r == l:
        # only one element, return the infinity
        return MAX_DISTANCE
    mid = l + (r - l) // 2

    x_mid = pts[mid][0]
    d1 = min_dist(pts, l, mid)
    d2 = min_dist(pts, mid+1, r)

    d = min(d1, d2)

    cross_l, cross_r = x_within_distance(pts, l, r, x_mid, d)
    d3 = MAX_DISTANCE

    if cross_l == None:
        # there is no points in the center zone
        pass
    else:
        sub_pts = sorted(pts[cross_l:cross_r+1], key=lambda x: x[1])
        sub_n = cross_r - cross_l + 1
        for i in range(0, sub_n):
            j = 1
            while (i + j < sub_n) and j <= 7:
                can_d = distance(sub_pts[i], sub_pts[i+j])
                if can_d < d3:
                    d3 = can_d
                j += 1

    return min(d, d3)


def distance(p1, p2):
    """
    Helper function to calculate the distance between two points.

    Args:
        p1 (tuple): (x1, y1).

        p2 (tupel): (x2, y2)

    Returns:
        float.
    """
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def x_within_distance(pts, l, r, ref, d):
    """
    Helper function to find the index range from the given points (sorted r.w.t x)
    s.t. the distance of them to the ref line (x=ref) is smaller than d.

    Args:
        pts (list of tuples): [(x1, y1), (x2, y2), ..(xn, yn)], sorted by x.

        l (int): left boundary index.

        r (int): right boundary index.

        ref (float): x = ref line.

        d (float): given distance.

    Returns:
        (left, right), the window (both inclusive) of the required points.
    """
    # TODO this can be improved using binary search.

    left = None
    right = None

    for i in range(l, r+1):
        if abs(pts[i][0] - ref) < d and (left == None):
            left = i

        if abs(pts[i][0] - ref) < d:
            right = i
    return left, right


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
