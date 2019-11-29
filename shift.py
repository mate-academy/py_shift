"""Shift module."""
from typing import List


def shift(array: List[int], num: int) -> List[int]:
    """shifts a list to the left by a given number of elements."""
    if num > len(array):
        raise ValueError
    if array:
        return array[num:] + array[:num]
    return []
