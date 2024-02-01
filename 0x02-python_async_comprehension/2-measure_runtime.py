#!/usr/bin/env python3
"""
import async_comprehension from prev
measure_routine() executes async_comprehension
four times in parallel using asyncio.gather.
it measures the total runtime
return the total runtime

"""
import asyncio
import time
import random
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """function that measures the total runtime
    of async_comprehension"""
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()
    return end - start
