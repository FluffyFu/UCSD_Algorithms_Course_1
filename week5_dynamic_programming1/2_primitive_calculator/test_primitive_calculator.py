import pytest
from primitive_calculator import optimal_sequence


def test_optimal_sequence():

    n = 1
    assert optimal_sequence(n) == [1]

    n = 5
    result = optimal_sequence(n)
    assert result in [[1, 2, 4, 5], [1, 3, 4, 5]]

    n = 96234
    result = optimal_sequence(n)
    assert len(result) == len([1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039,
                               32078, 96234])

