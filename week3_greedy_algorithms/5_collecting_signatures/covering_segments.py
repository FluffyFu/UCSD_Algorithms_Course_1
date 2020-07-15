# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    """
    Given a list of intervals (defined by integers). Find the minimum number of points,
    such that each segment at least contains one point.

    Args:
        segments (list of namedtuples): a list of [a_i, b_i] intervals, both of them are integers
        and a_i <= b_i

    Returns:
        a list of points that fulfills the requirement.
    """
    points = []
    sorted_segments = sorted(segments, key=lambda x: x.start)
    end = sorted_segments[0].end

    for current in sorted_segments:
        if current.start > end:
            points.append(end)
            end = current.end
        elif current.end < end:
            end = current.end
    points.append(end)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(
        x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
