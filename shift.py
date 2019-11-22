"""
shift module
"""
from typing import List


def shift(lst: List[int], num: int) -> List[int]:
    """
    Perform a circular shift of a list to the left by a given number of elements.
    :param lst: List[int]
    :param num: int
    :return: List[int]
    """
    if not lst:
        return lst
    if num > len(lst):
        raise ValueError
    num = num % len(lst)
    return lst[num:] + lst[:num]
