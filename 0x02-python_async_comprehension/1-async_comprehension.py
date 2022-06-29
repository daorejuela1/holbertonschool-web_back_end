#!/usr/bin/env python3
"""
Prints the data from the async generator
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Prints yielded values from the async generator
    """
    result = []
    async for i in async_generator():
        result.append(i)
    return(result)
