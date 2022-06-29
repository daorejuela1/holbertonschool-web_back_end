#!/usr/bin/env python3
"""
Prints the data from the async generator
"""
from time import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Prints yielded values from the async generator
    """
    start = time()
    number_of_executions = 4
    await gather(*[async_comprehension() for _ in range(number_of_executions)])
    end = time()
    return(end - start)
