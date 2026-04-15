"""
Convert a format of color to another format.

* RGB: tuple, (Red, Green, Blue)
* HSL: tuple, (Hue, Saturation, Lightness)
* RGBA: tuple, (Red, Green, Blue, Alpha)
* HEX: hexadecimal, such as '#ABCDEF' or '#12345678'
* NAME: string, such as 'royalblue'
"""

from __future__ import annotations
import colorsys
import math
from ..core import configs
from . import colortable, rgb

def rgb_to_hex(value: tuple[int, int, int]) -> str:
    """
    Convert a RGB code to a hexadecimal code.
    
        Args:
            value: a RGB code.
    
        Returns:
            A hexadecimal code.
    """

def hex_to_rgb(value: str) -> tuple[int, int, int]:
    """
    Convert a hexadecimal code to a RGB code.
    
        Args:
            value: a hexadecimal code.
    
        Returns:
            A RGB code.
    """

def rgba_to_hex(value: tuple[int, int, int, float]) -> str:
    """
    Convert a RGBA code to a hexadecimal code.
    
        Args:
            value: a RGBA code.
    
        Returns:
            A hexadecimal code.
    """

def hex_to_rgba(value: str) -> tuple[int, int, int, float]:
    """
    Convert a hexadecimal code to a RGBA code.
    
        Args:
            value: a hexadecimal code.
    
        Returns:
            A RGBA code.
    """

def rgb_to_rgba(value: tuple[int, int, int]) -> tuple[int, int, int, float]:
    """
    Convert a RGB code to a RGBA code.
    
        Args:
            value: a RGB code.
    
        Returns:
            A RGBA code with alpha channel ``0``.
    """

def rgba_to_rgb(value: tuple[int, int, int, float], refer: tuple[int, int, int]) -> tuple[int, int, int]:
    """
    Convert a RGBA code to a RGB code.
    
        Args:
            value: a RGBA code.
            refer: a RGB code as the background.
    
        Returns:
            A RGB code blended with the background.
    """

def hsl_to_rgb(value: tuple[float, float, float]) -> tuple[int, int, int]:
    """
    Convert a HSL code to a RGB code.
    
        Args:
            value: a HSL code.
    
        Returns:
            A RGB code.
    """

def rgb_to_hsl(value: tuple[int, int, int]) -> tuple[float, float, float]:
    """
    Convert a RGB code to a HSL code.
    
        Args:
            value: a RGB code.
    
        Returns:
            A HSL code.
    """

def hsl_to_hex(value: tuple[float, float, float]) -> str:
    """
    Convert a HSL code to a hexadecimal code.
    
        Args:
            value: a HSL code.
    
        Returns:
            A hexadecimal code.
    """

def hex_to_hsl(value: str) -> tuple[float, float, float]:
    """
    Convert a hexadecimal code to a HSL code.
    
        Args:
            value: a hexadecimal code.
    
        Returns:
            A HSL code.
    """

def name_to_rgb(value: str) -> tuple[int, int, int]:
    """
    Convert a color name to a RGB code.
    
        Args:
            value: a color name.
    
        Returns:
            A RGB code.
    """

def rgb_to_name(value: tuple[int, int, int]) -> list[str]:
    """
    Convert a RGB code to a color name.
    
        Args:
            value: a RGB code.
    
        Returns:
            A list of color names.
    """

def name_to_hex(value: str) -> str:
    """
    Convert a color name to a hexadecimal code.
    
        Args:
            value: a color name.
    
        Returns:
            A hexadecimal code.
    """

def hex_to_name(value: str) -> list[str]:
    """
    Convert a hexadecimal code to a color name.
    
        Args:
            value: a hexadecimal code.
    
        Returns:
            A list of color names.
    """

def fix_hex_length(value: str) -> str:
    """
    Fix the length of a hexadecimal code.
    
        Args:
            value: a hexadecimal code.
    
        Returns:
            A fixed hexadecimal code.
    """

def str_to_rgb(value: str) -> tuple[int, int, int]:
    """
    Convert a color name or a hexadecimal code to a RGB code.
    
        Args:
            value: a color name or a hexadecimal code.
    
        Returns:
            A RGB code.
    """
