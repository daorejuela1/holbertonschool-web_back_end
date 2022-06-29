#!/usr/bin/env python3
"""
Prints the data from the async generator
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Prints yielded values from the async generator
    """
    return [i async for i in async_generator()]
