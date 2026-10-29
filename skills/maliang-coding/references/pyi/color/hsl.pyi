"""
Some functions about HSL codes.
"""

from __future__ import annotations
import math
import operator
import statistics
from typing import TYPE_CHECKING
from ..animation import controllers
from collections.abc import Callable

def contrast(value: tuple[float, float, float], channels: tuple[bool, bool, bool]) -> tuple[float, float, float]:
    """
    Get the contrasting color of a HSL code.
    
        Args:
            value: a HSL code.
            channels: three color channels.
    
        Returns:
            The contrasting color of a HSL code.
    """

def transition(first: tuple[float, float, float], second: tuple[float, float, float], rate: float, channels: tuple[bool, bool, bool]) -> tuple[float, float, float]:
    """
    Transition one color to another proportionally.
    
        Args:
            first: the first HSL code.
            second: the second HSL code.
            rate: transition rate.
            channels: three color channels.
    
        Returns:
            The transitioned HSL code.
    """

def blend(*values: tuple[float, float, float], weights: list[float] | None) -> tuple[float, float, float]:
    """
    Mix colors by weight.
    
        Args:
            values: HSL codes.
            weights: weight list, default value indicates the same weights.
    
        Returns:
            The blended HSL code.
    """

def gradient(first: tuple[float, float, float], second: tuple[float, float, float], count: int, rate: float, channels: tuple[bool, bool, bool], controller: Callable[[float], float]) -> list[tuple[float, float, float]]:
    """
    Get a list of color gradients from one color to another proportionally.
    
        Args:
            first: the first HSL code.
            second: the second HSL code.
            count: the number of gradients.
            rate: transition rate.
            channels: three color channels.
            controller: control function.
    
        Returns:
            A list of color gradients.
    """
