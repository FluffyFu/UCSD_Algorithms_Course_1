from placing_parentheses import get_maximum_value, min_max_sub_value, extract_digits_and_operations
import pudb


def test_get_maximum_value():
    dataset = "1+5"
    assert get_maximum_value(dataset) == 6

    dataset = "5-3*2"
    assert get_maximum_value(dataset) == 4

    dataset = "5-8+7*4"
    assert get_maximum_value(dataset) == 25

    dataset = "5-8+7*4-8+9"
    assert get_maximum_value(dataset) == 200
