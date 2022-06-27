#!/usr/bin/env python3
"""
Method to safely get a value
"""
from typing import Any, Mapping, TypeVar, Union, NoneType


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[TypeVar, NoneType] = None,
) -> Union[TypeVar, NoneType]:
    """
    method to safely get a value
    """
    if key in dct:
        return dct[key]
    else:
        return default
