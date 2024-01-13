#!/usr/bin/env python3
"""
typed annotated function that takes a list of floats as arg
return the sum of the list
"""
from typing  import List

def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of numbers"""
    return sum(input_list) 
