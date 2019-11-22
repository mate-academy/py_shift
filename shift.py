# from typing import List
"""module docstring"""


def shift(list_of_numbers, num):
    """func docstring"""
    if num > len(list_of_numbers):
        raise ValueError
    shifted_list = list_of_numbers.copy()
    for seq, value in enumerate(list_of_numbers):
        new_seq = seq - num
        if new_seq < 0:
            new_seq = seq - num + len(list_of_numbers)
        shifted_list[new_seq] = value

    return shifted_list
