"""module to perform a circular shift of a list to the left by a given number of elements."""
from typing import List


def shift(array: List[int], num: int) -> List[int]:
    """function to perform a circular shift of a list to the left by a given number of elements."""
    if num > len(array):
        raise ValueError
    for _ in range(num):
        array.append(array.pop(0))
    return array
