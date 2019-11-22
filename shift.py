"""
docstring
"""
from typing import List


def shift(lst: List[int], num: int) -> List[int]:
    """

    :param lst:
    :param num:
    :return:
    """
    if num > len(lst):
        raise ValueError
    return lst[num:] + lst[:num]
