#!/usr/bin/env python3
"""
typed annotated funtion that takes a string 
and int  OR  float as ags and retrun a tuples
the first element of the tuple is the string(k)
the second element is the square of int or float(v)
the second element should be annotated as a float
"""
from typing import Union, Tuple


def to_kv(k: Union[str, int, float], v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the string and its square"""
    return (str(k), v ** 2) 