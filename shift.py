"""The function to perform a circular shift of a list to the left by a given
number of elements.
"""

from typing import List


def shift(arr: List[int], num: int) -> List[int]:
    """General func"""
    if not num:
        return arr
    if num > len(arr):
        raise ValueError
    for _i in range(num):
        value = arr.pop(0)
        arr.append(value)
    return arr
