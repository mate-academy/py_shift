"""
docstring
"""
import pytest

import shift


def test_empty():
    """

    :return:
    """
    assert shift.shift([], 0) == []


def test_one():
    """

    :return:
    """
    assert shift.shift([1, 2, 3], 1) == [2, 3, 1]


def test_two():
    """

    :return:
    """
    assert shift.shift([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test_to_many_shifts():
    """

    :return:
    """
    with pytest.raises(ValueError):
        assert shift.shift([1, 2, 3], 5)
