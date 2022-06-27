#!/usr/bin/env python3
"""
Method to safely get a value
"""
from typing import Any, Mapping, Optional, TypeVar


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Optional[TypeVar] = None,
) -> Optional[TypeVar]:
    """
    method to safely get a value
    """
    if key in dct:
        return dct[key]
    else:
        return default
