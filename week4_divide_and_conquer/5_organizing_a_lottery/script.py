from points_and_segments import binary_search, single_line_cross, fast_count_segments, naive_count_segments
import numpy as np

k = 5000
n = int(1E4)
starts = [-1] * n
ends = [n] * n
points = np.random.randint(low=0, high=n, size=k)
fast_count_segments(starts, ends, points)
