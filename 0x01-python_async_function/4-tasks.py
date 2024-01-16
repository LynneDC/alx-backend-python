#!/usr/bin/env python3
"""
Execute task_wait_random n times with the specified max_delay.
Args:
    n (int): The number of times to execute task_wait_random.
    max_delay (int): The maximum delay to pass to task_wait_random
Returns:
    List[float]: A sorted list of delays from executing task_wait_random.
"""
import asyncio
import random
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        List[float]: A sorted list of delays from executing task_wait_random.
    """
    delays = []
    for _ in range(n):
        delays.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*delays))
