#!/usr/bin/env python3
"""
import previous wait_n function
create measure_time function with int n and max_delay args that
measures the total execution time for wait(n, max_delay)
and retuns total_time / n
return a float
use time module to measure time elapse
"""
import time
import asyncio

wait_n =  __import__("1-concurrent_coroutine").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    parameters:
    n (int): The number of iterations to run wait_n for.
    max_delay (int): The max_delay argument to pass to wait_n.
    Returns:
        float: The total execution time divided by n.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return(end - start) / n 