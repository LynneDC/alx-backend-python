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

""" defining a function that takesno arguments and returns a coroutine """
async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)