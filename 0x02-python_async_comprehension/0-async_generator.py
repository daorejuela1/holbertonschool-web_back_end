#!/usr/bin/env python3
"""
Async random number generator
"""
from random import uniform
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator
    """
    for _ in range(10):
        random_number: float = uniform(0, 10)
        await sleep(1)
        yield random_number
