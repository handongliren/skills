"""
Some useful utility classes or utility functions.
"""

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
from typing import TYPE_CHECKING
from ..core import configs, virtual
from . import enhanced
from PIL import Image
from collections.abc import Callable
from typing import Any

class Trigger:
    """
    Single trigger.
    
        It can only be triggered once before the reset, and multiple triggers are
        invalid. When triggered, the callback function is called.
    """

    def __init__(self, command: Callable[..., Any]) -> None:
        """
        Args:
                    command: the function that is called when triggered.
        """
    def get(self) -> bool:
        """
        Get the status of the trigger.
        """
    def reset(self) -> None:
        """
        Reset the status of the trigger.
        """
    def lock(self) -> None:
        """
        Lock the trigger so that it can't be updated.
        """
    def unlock(self) -> None:
        """
        Unlock this trigger so that it can be updated again.
        """
    def update(self, value: bool, *args: Any, **kwargs: Any) -> None:
        """
        Update the status of the trigger.
        
                Args:
                    value: updated value.
                    args: args of the command.
                    kwargs: kwargs of the command.
        """

def get_parent(widget: tkinter.Misc) -> int:
    """
    Get the HWND of ``tkinter.Widget``.
    
        Args:
            widget: the widget.
    
        Returns:
            The HWND of the widget.
    """

def embed_window(window: tkinter.Misc, parent: tkinter.Misc | None, focus: bool) -> None:
    """
    Embed a widget into another widget.
    
        Args:
            window: Widget that will be embedded in.
            parent: parent widget, ``None`` indicates that the parent widget is the
                screen.
            focus: whether direct input focus to this window.
    """

def load_font(font_path: str | bytes, private: bool, enumerable: bool) -> bool:
    """
    Make fonts located in file ``font_path`` available to the font system.
    
        Args:
            font_path: the font file path.
            private: if True, other processes cannot see this font(Only Windows OS),
                and this font will be unloaded when the process dies.
            enumerable: if True, this font will appear when enumerating
                fonts(Only Windows OS).
    
        Returns:
            Whether the operation succeeds.
    
        Warning:
            This function only works on Windows and Linux OS.
    
        Note:
            This function is referenced from ``customtkinter.load_font``,
                ``customtkinter``: https://github.com/TomSchimansky/CustomTkinter.
    """

def screen_size() -> tuple[int, int]:
    """
    Returns the size of the screen.
    """

def get_text_size(text: str, fontsize: int | None, family: str | None, padding: int, wrap_length: int | None, font: tkinter.font.Font | None, master: tkinter.Canvas | virtual.Widget | None, **kwargs: Any) -> tuple[int, int]:
    """
    Get the size of a text with a special font family and font size.
    
        Args:
            text: the text.
            fontsize: font size of the text.
            family: font family of the text.
            padding: extra padding of the size.
            wrap_length: limit the length of text, beyond which it will
                automatically wrap.
            font: font object to use (if ``None``, a new font will be created).
            master: default canvas or widget provided.
            kwargs: additional keyword arguments for the font.
    
        Warning:
            This function only works when the fontsize is negative number!
    """

def fix_cursor(name: str) -> str:
    """
    Fix the cursor name.
    
        Args:
            name: name of cursor
    
        Returns:
            Fixed cursor name.
    """

def create_smoke(size: tuple[int, int], color: str | tuple[int, int, int, int]) -> enhanced.PhotoImage:
    """
    Create a temporary smoke zone. Return the ``enhanced.PhotoImage``.
    
        Args:
            size: size of the smoke zone.
            color: color of the smoke zone.
    
        Returns:
            Enhanced photo image of the smoke zone.
    
        Raises:
            RuntimeError: If the ``PIL`` package is not installed.
    
        Warning:
            This function need ``PIL`` to run.
    
        Tip:
            About the "smoke", see: https://fluent2.microsoft.design/material#smoke
    """
