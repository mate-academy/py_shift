import pytest

import shift


def test_empty():
    assert shift.shift([], 0) == []


def test_one():
    assert shift.shift([1, 2, 3], 1) == [2, 3, 1]


def test_two():
    assert shift.shift([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test_to_many_shifts():
    with pytest.raises(ValueError):
        assert shift.shift([1, 2, 3], 5)