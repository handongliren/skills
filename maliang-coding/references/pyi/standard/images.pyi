"""All standard ``Image`` classes."""

from __future__ import annotations
from typing import Any
from typing_extensions import override
from ..core import virtual
from ..toolbox import enhanced
from PIL import Image

class StillImage(virtual.Image):
    """A simple still image."""

    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...

class Smoke(virtual.Image):
    """A special Image with only one color."""

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, color: str | None, name: str | None, animation: bool, **kwargs: Any) -> None: ...
    @override
    def display(self) -> None: ...
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None: ...
