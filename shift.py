"""
shift
"""
from typing import List

def shift(numbers: List[int], num: int) -> List[int]:
    """
    :param numbers: [int] list of numbers
    :param num: int times to shift
    :return: [int] new list
    """
    if num > len(numbers):
        raise ValueError

    new_numbers = numbers.copy()

    for _ in range(num):
        shifted_element = new_numbers.pop(0)
        new_numbers.append(shifted_element)

    return new_numbers
