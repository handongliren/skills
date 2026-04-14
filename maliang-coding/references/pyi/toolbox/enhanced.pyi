"""Enhanced versions of some ``tkinter`` classes and functions."""

from __future__ import annotations
import functools
import tkinter
from PIL import ImageTk

class PhotoImage(tkinter.PhotoImage):
    """Enhanced version of ``tkinter.PhotoImage``."""

    def scale(self, x: float, y: float) -> PhotoImage: ...
    def resize(self, width: int, height: int) -> PhotoImage: ...

class PhotoImage(ImageTk.PhotoImage, tkinter.PhotoImage):
    """Pillow version of ``tkinter.PhotoImage``."""

    def scale(self, x: float, y: float) -> PhotoImage: ...
    def resize(self, width: int, height: int) -> PhotoImage: ...
