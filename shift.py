"""Perform a circular shift of a list"""
from typing import List


def shift(array: List[int], num: int) -> List[int]:
    """Function to perform a circular shift of a list to the left by a given number of elements"""
    if num > len(array):
        raise ValueError
    started_slice = array[0:num]
    rest_list = array[num::]
    return [*rest_list, *started_slice]
