"""Some functions about HSL codes."""

from __future__ import annotations
import math
import operator
import statistics
from collections.abc import Callable
from ..animation import controllers

def contrast(value: tuple[float, float, float], channels: tuple[bool, bool, bool]) -> tuple[float, float, float]: ...

def transition(first: tuple[float, float, float], second: tuple[float, float, float], rate: float, channels: tuple[bool, bool, bool]) -> tuple[float, float, float]: ...

def blend(*values: tuple[float, float, float], weights: list[float] | None) -> tuple[float, float, float]: ...

def gradient(first: tuple[float, float, float], second: tuple[float, float, float], count: int, rate: float, channels: tuple[bool, bool, bool], controller: Callable[[float], float]) -> list[tuple[float, float, float]]: ...
