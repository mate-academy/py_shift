'''
Module
'''
from typing import List


def shift(lst: List[int], num: int) -> List[int]:
    '''

    :param lst:
    :param num:
    :return:
    '''
    lngth = len(lst)
    if num > lngth:
        raise ValueError
    if num == lngth:
        return lst
    return lst[num:] + lst[:num]
