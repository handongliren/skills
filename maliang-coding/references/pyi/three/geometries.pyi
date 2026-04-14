"""Standard Geometries"""

from __future__ import annotations
from . import engine

class Cuboid(engine.Geometry):
    """Cuboid"""

    def __init__(self, canvas: engine.Canvas | engine.Space, x: float, y: float, z: float, length: float, width: float, height: float, boardwidth: int, color_fill_up: str, color_fill_down: str, color_fill_left: str, color_fill_right: str, color_fill_front: str, color_fill_back: str, color_outline_up: str, color_outline_down: str, color_outline_left: str, color_outline_right: str, color_outline_front: str, color_outline_back: str) -> None: ...

class Tetrahedron(engine.Geometry):
    """Tetrahedron"""

    def __init__(self, canvas: engine.Canvas | engine.Space, point_1: tuple[float, float, float], point_2: tuple[float, float, float], point_3: tuple[float, float, float], point_4: tuple[float, float, float], boardwidth: int, color_fill: tuple[str, str, str, str], color_outline: tuple[str, str, str, str]) -> None: ...
