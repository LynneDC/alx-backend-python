#!/usr/bin/env python3
"""
coroutine called <code>async_generator</code>
takes no arguments
loops 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10
using the random module
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ defining a function that takes no arguments
    and returns a coroutine """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
