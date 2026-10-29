"""
Controller generator and standard control functions.

Definition of control function:

    def control_function(t: float, /) -> float:
        """Control function for animation.

        Args:
            t: the percentage of time.

        Returns:
            a multiple of the cardinality of the animation.
        """
"""

from __future__ import annotations
import functools
import math
import warnings
from typing import TYPE_CHECKING, overload
from collections.abc import Callable
from typing import Literal

def generate(base: Callable[[float], float], start: float, end: float) -> Callable[[float], float]:
    ...

def generate(base: Callable[[float], float], start: float, end: float, map_y: Literal[False]) -> Callable[[float], float]:
    ...

def generate(base: Callable[[float], float], start: float, end: float, map_y: bool) -> Callable[[float], float]:
    """
    Generate a control function from an ordinary mathematical function.
    
        Args:
            base: base function, an ordinary mathematical function.
            start: the first value of the parameter of the base function.
            end: the last value of the parameter of the base function.
            map_y: whether map the final return value to ``1``.
    
        Returns:
            A control function.
    """

def linear(t: float) -> float:
    """
    Speed remains the same.
    """

def smooth(t: float) -> float:
    """
    Speed is slow first, then fast and then slow. (slow -> fast -> slow)
    """

def rebound(t: float) -> float:
    """
    Before the end, displacement will bounce off a bit.
    """

def ease_in(t: float) -> float:
    """
    Gradually accelerate. (slow -> fast)
    """

def ease_out(t: float) -> float:
    """
    Gradually decelerate. (fast -> slow)
    """
