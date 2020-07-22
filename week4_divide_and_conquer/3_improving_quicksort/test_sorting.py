from sorting import partition3, randomized_quick_sort_2, randomized_quick_sort
from hypothesis import given, settings, assume
from hypothesis import strategies


def test_partition3():
    a = [2, 2, 3, 1]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (1, 2)

    a = [2, 2, 2, 1]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (1, 3)

    a = [2, 2, 3, 2]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (0, 2)

    a = [2]
    l, r = 0, len(a) - 1
    assert partition3(a, l, r) == (0, 0)


@given(a=strategies.lists(strategies.integers(min_value=1, max_value=int(1E8))))
@settings(max_examples=100)
def test_randomized_quick_sort(a):
    assume(len(a) > 0)
    l, r = 0, len(a) - 1
    assert randomized_quick_sort_2(a, l, r) == randomized_quick_sort(a, l, r)
