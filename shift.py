"""docstring"""
from typing import List


def shift(input_list: List[int], num: int) -> List[int]:
    """docstring"""

    if len(input_list) < num:
        raise ValueError

    return input_list[num:] + input_list[:num]
