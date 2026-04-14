"""Controller generator and standard control functions.

Definition of control function::

    def control_function(t: float, /) -> float:
        '''Control function for animation.

        Args:
            t: the percentage of time.

        Returns:
            a multiple of the cardinality of the animation.
        '''
"""

from __future__ import annotations
import functools
import math
import warnings
from collections.abc import Callable
from typing import Literal, overload

def generate(base: Callable[[float], float], start: float, end: float) -> Callable[[float], float]: ...

def generate(base: Callable[[float], float], start: float, end: float, map_y: Literal[False]) -> Callable[[float], float]: ...

def generate(base: Callable[[float], float], start: float, end: float, map_y: bool) -> Callable[[float], float]: ...

def linear(t: float) -> float: ...

def smooth(t: float) -> float: ...

def rebound(t: float) -> float: ...

def ease_in(t: float) -> float: ...

def ease_out(t: float) -> float: ...
