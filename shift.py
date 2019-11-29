"""shift for many position"""
from typing import List


def shift(item_list: List[int], num: int) -> List[int]:
    """something to do"""
    if num > len(item_list):
        raise ValueError

    left = [i for i in item_list if item_list.index(i) < num]
    right = [i for i in item_list if item_list.index(i) > num - 1]
    right.extend(left)
    return right
