#!/usr/bin/env python3
"""
an async routine called wait_n that takes 2 int args in this order:
    n and max_delay
spawn wait_random n times with the specified max_delay
wait_n returns the list of all the delays in float values.
the list of delays should be in ascending order
do not use sort()because of concurrency
"""
import asyncio
import random
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n retunrs the list of all the delays in float values.
    """
    delays = []
    for _ in range(n):
        delays.append(asyncio.create_task(wait_random(max_delay)))
    return sorted(await asyncio.gather(*delays))
