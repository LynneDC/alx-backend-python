#!/usr/bin/env python3
"""
typed annotated funtion that takes a float multiplier as arg
return a function that multiply a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiply a float by multiplier"""
    def multiply(n: float) -> float:
        """Return the multiplication of a number and a multiplier"""
        return n * multiplier
    return multiply
