"""
import async_comprehension from prev
measure_routine() executes async_comprehension four times in parallel using asyncio.gather.
it measures the total runtime 
return the total runtime

"""
import asyncio
import time
import random
from 1-async_comprehension import async_comprehension

"""function that measures the total runtime of async_comprehension"""
async def measure_routine():
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()