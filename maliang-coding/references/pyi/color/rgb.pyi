"""Some functions about RGB codes."""

from __future__ import annotations
import operator
import statistics
from collections.abc import Callable
from ..animation import controllers

def contrast(value: tuple[int, int, int], channels: tuple[bool, bool, bool]) -> tuple[int, int, int]: ...

def transition(first: tuple[int, int, int], second: tuple[int, int, int], rate: float, channels: tuple[bool, bool, bool]) -> tuple[int, int, int]: ...

def blend(*values: tuple[int, int, int], weights: list[float] | None) -> tuple[int, int, int]: ...

def gradient(first: tuple[int, int, int], second: tuple[int, int, int], count: int, rate: float, channels: tuple[bool, bool, bool], controller: Callable[[float], float]) -> list[tuple[int, int, int]]: ...
