#!/usr/bin/env python3
"""
fuction that takes a list lst
and retrun a list of tuplescontaining two elemeents
i from the input list and its lenghth an int
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the string and its length"""
    return [(i, len(i)) for i in lst]
