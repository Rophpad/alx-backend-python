#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns a sum(of type float)
    of elements(of type float) in a list
    """
    sum_list: float = 0.0
    for num in input_list:
        sum_list += num
    return sum_list
