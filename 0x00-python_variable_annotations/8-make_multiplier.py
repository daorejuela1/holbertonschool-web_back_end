#!/usr/bin/env python3
"""
Function to call a multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function to call a multiplier function
    """
    def multiplier_f(multiplier: float) -> float:
        """
        Multiplies the input by n
        """
        return 2.22 * multiplier
    return multiplier_f
