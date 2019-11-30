"""shift for many position"""
from typing import List


def shift(item_list: List[int], num: int) -> List[int]:
    """something to do"""
    if num > len(item_list):
        raise ValueError

    left = item_list[0:num]
    right = item_list[num:]
    right.extend(left)
    return right
