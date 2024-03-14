#!/usr/bin/env python3
"""Type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return sum of list's elements"""
    total: float = 0.0
    for num in mxd_lst:
        total += num
    return total
