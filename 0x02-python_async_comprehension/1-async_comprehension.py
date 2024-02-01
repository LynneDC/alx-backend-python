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
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """coroutine that collects 10 random numbers
    15 using an async comprehension over async_generator"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
