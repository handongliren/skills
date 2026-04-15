"""
All standard ``Image`` classes.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
from typing_extensions import override
from ..core import virtual
from ..toolbox import enhanced
from PIL import Image
from typing import Any

class StillImage(virtual.Image):
    """
    A simple still image.
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

class Smoke(virtual.Image):
    """
    A special Image with only one color.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, color: str | None, name: str | None, animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    color: color of the image object of the element.
                    name: name of element.
                    animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        
                Raises:
                    RuntimeError: If the ``pillow`` package is not installed.
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
