#!/usr/bin/env python3
"""
Async random number generator
"""
from random import uniform


async def async_generator() -> float:
    """
    Async generator
    """
    for _ in range(10):
        yield uniform(0, 10)
