#!/usr/bin/env python3
"""
import async_generator from task 0
async_comprehension takes no argument
coroutine collects 10 random numbers
using an async comprehensing over async_generator
return the 10 random numbers
"""
import asyncio
import random
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """coroutine that collects 10 random numbers
    using an async comprehension over async_generator"""
    return [random async for random in async_generator()]
