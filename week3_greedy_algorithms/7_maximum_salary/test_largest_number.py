from largest_number import largest_number_naive, is_greater, largest_number
import pytest
from hypothesis import given, settings, assume
import hypothesis.strategies as st


@given(a=st.lists(st.integers(min_value=1, max_value=1000)))
@settings(max_examples=100)
def test_largest_number_random(a):
    assume(len(a) > 0)
    str_a = [str(i) for i in a]
    assert largest_number(str_a) == largest_number_naive(str_a)


# @pytest.mark.repeat(100)
def test_largest_number_naive():
    a = ['21', '2'] * 1000
    assert largest_number_naive(a) == '2' * 1000 + '21' * 1000

    a = ['9', '4', '6', '1', '9']
    assert largest_number_naive(a) == '99641'

    a = ['23', '39', '92']
    assert largest_number_naive(a) == '923923'


# @pytest.mark.repeat(100)
def test_largest_number():
    a = ['21', '2'] * 1000
    assert largest_number(a) == '2' * 1000 + '21' * 1000

    a = ['9', '4', '6', '1', '9']
    assert largest_number(a) == '99641'

    a = ['23', '39', '92']
    assert largest_number(a) == '923923'

    a = ['1']
    assert largest_number(a) == '1'


def test_is_greater():
    assert is_greater('21', '2') == -1
    assert is_greater('2', '21') == 1
    assert is_greater('23', '2') == 1
    assert is_greater('223', '2') == 1
    assert is_greater('221', '2') == -1
    assert is_greater('221', '22') == -1
    assert is_greater('1231', '123') == -1
    assert is_greater('1123112311', '1123')
    assert is_greater('1112', '11') == 1
    assert is_greater('22', '2') == 0
    assert is_greater('22', '22') == 0
