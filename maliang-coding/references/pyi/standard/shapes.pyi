"""All standard ``Shape`` classes."""

from __future__ import annotations
import math
import warnings
from typing import Any, Literal
from typing_extensions import override
from ..core import virtual

class Line(virtual.Shape):
    """Create a line for a widget."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, points: list[tuple[float, float]] | None, name: str | None, gradient_animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class Rectangle(virtual.Shape):
    """Create a rectangle for a widget."""

    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class Oval(virtual.Shape):
    """Create a oval for a widget"""

    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...
    @override
    def detect(self, x: float, y: float) -> bool: ...

class Arc(virtual.Shape):
    """Create a arc for a widget."""

    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class RegularPolygon(virtual.Shape):
    """Create a regular polygon for a widget."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, side: int, angle: float, name: str | None, gradient_animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class RoundedRectangle(virtual.Shape):
    """Create a rounded rectangle for a widget."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, radius: int, name: str | None, gradient_animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class HalfRoundedRectangle(virtual.Shape):
    """Create a half rounded rectangle for a widget."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, radius: int, ignore: Literal['left', 'right'], name: str | None, gradient_animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class SemicircularRectangle(virtual.Shape):
    """Create a semicircular rectangle for a widget."""

    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...
    @override
    def detect(self, x: float, y: float) -> bool: ...

class SharpRectangle(virtual.Shape):
    """Create a sharp rectangle for a widget."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, theta: float, ratio: tuple[float, float], name: str | None, gradient_animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class Parallelogram(virtual.Shape):
    """Create a parallelogram for a widget."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, theta: float, name: str | None, gradient_animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...
