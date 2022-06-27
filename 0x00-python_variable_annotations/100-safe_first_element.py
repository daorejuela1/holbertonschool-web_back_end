#!/usr/bin/env python3
"""
Obtains the first element of a list safely
"""
from typing import Any, Sequence, Union, Optional


def safe_first_element(lst: Optional[Sequence[Any]]) -> Union[Any, None]:
    """
    Obtains the first element of a list safely
    """
    if lst:
        return lst[0]
    else:
        return None
