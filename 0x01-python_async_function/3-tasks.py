#!/usr/bin/env python3
"""
write a function that takes an int max_delay and
return a asyncio.task
"""
from asyncio import Task, create_task


wait_n = __import__("0-basic_async_syntax").wait_n


def measure_time(n: int, max_delay: int) -> Task:
    """
    Returns:
    asyncio task
    """
    task = create_task(wait_n(max_delay))
    return task
