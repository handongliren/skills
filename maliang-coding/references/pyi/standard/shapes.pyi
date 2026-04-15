"""
All standard ``Shape`` classes.
"""

from __future__ import annotations
import math
import warnings
from typing import TYPE_CHECKING
from typing_extensions import override
from ..core import virtual
from typing import Any, Literal

class Line(virtual.Shape):
    """
    Create a line for a widget.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, points: list[tuple[float, float]] | None, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    points: key points of line.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class Rectangle(virtual.Shape):
    """
    Create a rectangle for a widget.
    """

    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class Oval(virtual.Shape):
    """
    Create a oval for a widget
    """

    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """
    @override
    def detect(self, x: float, y: float) -> bool:
        """
        Detect whether the specified coordinates are within ``Element``.
        """

class Arc(virtual.Shape):
    """
    Create a arc for a widget.
    """

    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class RegularPolygon(virtual.Shape):
    """
    Create a regular polygon for a widget.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, side: int, angle: float, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    side: number of sides of a regular polygon.
                    angle: number of radians of a regular polygon rotated clockwise.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class RoundedRectangle(virtual.Shape):
    """
    Create a rounded rectangle for a widget.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, radius: int, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    radius: radius of the fillet.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class HalfRoundedRectangle(virtual.Shape):
    """
    Create a half rounded rectangle for a widget.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, radius: int, ignore: Literal['left', 'right'], name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    radius: radius of the fillet.
                    ignore: edges to ignore.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class SemicircularRectangle(virtual.Shape):
    """
    Create a semicircular rectangle for a widget.
    """

    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """
    @override
    def detect(self, x: float, y: float) -> bool:
        """
        Detect whether the specified coordinates are within ``Element``.
        """

class SharpRectangle(virtual.Shape):
    """
    Create a sharp rectangle for a widget.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, theta: float, ratio: tuple[float, float], name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    theta: number of radians of sharp corners.
                    ratio: height ratio of the left and right sharp corners.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """

class Parallelogram(virtual.Shape):
    """
    Create a parallelogram for a widget.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, theta: float, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    theta: number of radians that the parallelogram is inclined to.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """
