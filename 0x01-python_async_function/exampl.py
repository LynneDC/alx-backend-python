import asyncio
import time


"""
hellow word program exaple on how async IO works
"""
async def count():
    print("One")
    await asyncio.sleep(1)
    print("two")


async def main():
    # gather determine the concurrency
    await asyncio.gather(count(), count(), )


if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print("we are here ")
    print(f"{__file__} executed in {elapsed: 0.2f} seconds")

# using function blockages 
def count1():
    print("ROSE")
    time.sleep(1)
    print("LYNNE")

def main1():
    for _ in range(3):
        count1()


if __name__ == "__main__":
    s = time.perf_counter()
    main1()
    elapsed = time.process_time() -s
    print(f"{__file__} executed in {elapsed: 0.2f} seconds")

# syntax rules example
print("EXAMPLES ON THE SYTAX RULES")
async def f(x):
    y = await z(x)
    return y
    print("await and return allowed in coroutines ")

async def g(x):
    yield x
    print("this is an async generator")

#making a dunctiona coroutine 
#generator based older syntax
@asyncio.coroutine
def py34_coro():
    """Generator based coroutine older syntax"""
    yield from stuff()

# modern way
async def py35_coro():
    """Native coroutine"""
    await stuff()