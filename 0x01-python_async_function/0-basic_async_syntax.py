#!/usr/bin/env python3
"""
Asynchronous coroutine that takes in an int arg (max_delay)
max_delay has default value = 10  
asynchronous coroutine name is wait_random
it waits for a random delay between 0 and max_delay seconds (float value) 
and eventually returns it
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Wait randomly between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay 