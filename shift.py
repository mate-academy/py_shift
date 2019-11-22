"""docstring"""
from typing import List


def shift(input_list: List[int], num: int) -> List[int]:
    """docstring"""

    result = []
    strlen = len(input_list)
    if strlen < num:
        raise ValueError
    for i in range(strlen):
        j = (strlen - num + i - 1) % strlen
        result.append(input_list[j])

    return result
