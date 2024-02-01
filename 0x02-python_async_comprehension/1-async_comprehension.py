"""
import async_generator from task 0
async_comprehension takes no argument
coroutine collects 10 random numbers using an async comprehensing over async_generator
return the 10 random numbers
"""
import asyncio
import random
"""From prevous task, import async_generator"""
from 0-async_generator import async_generator

"""croutine that collects 10 random numbers using an async comprehension over async_generator"""
async def async_comprehension():
    result = []
    async for i in async_generator():
        result.append(i)
    return result