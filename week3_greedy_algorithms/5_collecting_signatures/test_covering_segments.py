from covering_segments import optimal_points, Segment


def test_optimal_points():
    segments = [Segment(1, 3), Segment(2, 5), Segment(3, 6)]
    points = optimal_points(segments)
    assert points == [3]

    segments = [Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]
    points = optimal_points(segments)
    assert points == [3, 6]

    segments = [Segment(1, 1), Segment(2, 5), Segment(3, 6)]
    points = optimal_points(segments)
    assert points == [1, 5]

    segments = [Segment(1, 1), Segment(1, 5), Segment(3, 6)]
    points = optimal_points(segments)
    assert points == [1, 6]
