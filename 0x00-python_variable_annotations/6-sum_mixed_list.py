#!/usr/bin/env python3
"""
typed annotated funtion that takes 
a list of intergers and floats as an arg
and return their sum as a float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum of a list of numbers"""
    return sum(mxd_list)