"""Some useful utility classes or utility functions."""

from __future__ import annotations
import atexit
import ctypes
import os
import platform
import shutil
import sys
import tkinter
import tkinter.font
import traceback
from collections.abc import Callable
from typing import Any
from ..core import configs, virtual
from . import enhanced
from PIL import Image

class Trigger:
    """Single trigger.

    It can only be triggered once before the reset, and multiple triggers are
    invalid. When triggered, the callback function is called."""

    def __init__(self, command: Callable[..., Any]) -> None: ...
    def get(self) -> bool: ...
    def reset(self) -> None: ...
    def lock(self) -> None: ...
    def unlock(self) -> None: ...
    def update(self, value: bool, *args: Any, **kwargs: Any) -> None: ...

def get_parent(widget: tkinter.Misc) -> int: ...

def embed_window(window: tkinter.Misc, parent: tkinter.Misc | None, focus: bool) -> None: ...

def load_font(font_path: str | bytes, private: bool, enumerable: bool) -> bool: ...

def screen_size() -> tuple[int, int]: ...

def get_text_size(text: str, fontsize: int | None, family: str | None, padding: int, wrap_length: int | None, font: tkinter.font.Font | None, master: tkinter.Canvas | virtual.Widget | None, **kwargs: Any) -> tuple[int, int]: ...

def fix_cursor(name: str) -> str: ...

def create_smoke(size: tuple[int, int], color: str | tuple[int, int, int, int]) -> enhanced.PhotoImage: ...
