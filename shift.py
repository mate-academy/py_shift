""""
function to perform a circular shift of a list to the left by a given number of elements
"""

from typing import List


def shift(final_list: List[int], num: int) -> List[int]:
    """perform a circular shift"""
    if len(final_list) < num:
        raise ValueError

    final_list = final_list[num:] + final_list[:num]

    return final_list
