#!/usr/bin/env python3
"""
fuction that takes a list lst
and retrun a list of tuplescontaining two elemeents
i from the input list and its lenghth an int
"""
def element_length(lst: list) -> list[tuple]:
    return [(i, len(i)) for i in lst]