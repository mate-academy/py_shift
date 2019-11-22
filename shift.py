"""Module shift"""
from typing import List


def shift(lis: List[int], num: int) -> List[int]:
    """
    Performs a circular shift of a list
    to the left by a given number of elements.
    """
    length = len(lis)

    if num > length:
        raise ValueError

    if length < 2:
        return lis

    for _ in range(num):
        first = lis[0]
        for idx in range(length - 1):
            lis[idx] = lis[idx + 1]
        lis[-1] = first

    return lis
