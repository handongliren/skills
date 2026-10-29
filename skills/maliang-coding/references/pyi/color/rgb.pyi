"""
Some functions about RGB codes.
"""

from __future__ import annotations
import operator
import statistics
from typing import TYPE_CHECKING
from ..animation import controllers
from collections.abc import Callable

def contrast(value: tuple[int, int, int], channels: tuple[bool, bool, bool]) -> tuple[int, int, int]:
    """
    Get the contrasting color of a RGB code.
    
        Args:
            value: a RGB code.
            channels: three color channels.
    
        Returns:
            The contrasting color of the input RGB code.
    """

def transition(first: tuple[int, int, int], second: tuple[int, int, int], rate: float, channels: tuple[bool, bool, bool]) -> tuple[int, int, int]:
    """
    Transition one color to another proportionally.
    
        Args:
            first: the first RGB code.
            second: the second RGB code.
            rate: transition rate.
            channels: three color channels.
    
        Returns:
            The transitioned RGB code.
    """

def blend(*values: tuple[int, int, int], weights: list[float] | None) -> tuple[int, int, int]:
    """
    Mix colors by weight.
    
        Args:
            values: RGB codes.
            weights: weight list, default value indicates the same weights.
    
        Returns:
            The blended RGB code.
    """

def gradient(first: tuple[int, int, int], second: tuple[int, int, int], count: int, rate: float, channels: tuple[bool, bool, bool], controller: Callable[[float], float]) -> list[tuple[int, int, int]]:
    """
    Get a list of color gradients from one color to another proportionally.
    
        Args:
            first: the first RGB code.
            second: the second RGB code.
            count: the number of gradients.
            rate: transition rate.
            channels: three color channels.
            controller: control function, default is linear.
    
        Returns:
            A list of color gradients from the first RGB code to the second RGB
                code.
    """
