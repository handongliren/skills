"""
All icons with base64 format
"""

from __future__ import annotations
import tkinter
import typing
import PIL.ImageTk
from maliang.toolbox import enhanced

def parse(light: str, dark: str) -> dict[str, dict[typing.Literal['light', 'dark'], enhanced.PhotoImage]]:
    """
    Parse the base64 data to `enhanced.PhotoImage` with diffrent themes.
    """
