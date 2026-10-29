"""
Support for theme.

* ``darkdetect``: https://pypi.org/project/darkdetect/
* ``pywinstyles``: https://pypi.org/project/pywinstyles/
* ``win32material``: https://pypi.org/project/win32material/
* ``hPyT``: https://pypi.org/project/hPyT/
"""

from __future__ import annotations
import ctypes.wintypes
import platform
import sys
import threading
import traceback
import warnings
from typing import TYPE_CHECKING
from ..core import configs
from ..toolbox import utility
import pywinstyles
import hPyT
import win32material
import tkinter
from collections.abc import Callable
from typing import Any, Literal
import darkdetect
import darkdetect._windows_detect
import darkdetect

def set_color_mode(mode: Literal['system', 'dark', 'light']) -> None:
    """
    Set the color mode of the program.
    
        Args:
            mode: it can be ``"light"``, ``"dark"``, and ``"system"``.
    
        Tip:
            ``"system"`` is the following system.
    """

def get_color_mode() -> Literal['dark', 'light']:
    """
    Get the color mode of the program.
    """

def register_event(func: Callable[..., Any], *args: Any) -> None:
    """
    Register a function to be called when the system accent color changes.
    
        When the system accent color changes, the registered function will be
        called, and the parameter is a boolean value indicating whether it is
        currently a dark theme.
    
        Args:
            func: callback function.
            args: extra arguments.
    """

def remove_event(func: Callable[..., Any]) -> None:
    """
    Remove a registered function.
    
        Args:
            func: callback function.
    """

def apply_file_dnd(window: tkinter.Tk, command: Callable[[str], Any]) -> None:
    """
    Apply file drag and drop in a widget.
    
        Args:
            window: the window which being customized.
            command: callback function, accept a parameter that represents the path
                of the file.
    
        Warning:
            This function is only works on Windows OS!
    """

def apply_theme(window: tkinter.Tk, theme: Literal['mica', 'acrylic', 'acrylic2', 'aero', 'transparent', 'optimised', 'win7', 'inverse', 'native', 'popup', 'dark', 'normal']) -> None:
    """
    Apply some Windows themes to the window.
    
        Args:
            window: the window which being customized.
            theme: different themes for windows.
    
        Warning:
            This function is only works on Windows OS! And some parameters are
            useless on Windows 7/10!
    """

def customize_window(window: tkinter.Tk, border_color: str | None, header_color: str | None, title_color: str | None, hide_title_bar: bool | None, hide_button: Literal['all', 'maxmin', 'none'] | None, disable_minimize_button: bool | None, disable_maximize_button: bool | None, border_type: Literal['rectangular', 'smallround', 'round'] | None) -> None:
    """
    Customize the relevant properties of the window
    
        Args:
            window: the window which being customized.
            border_color: border color of the window.
            header_color: header color of the window.
            title_color: title color of the window.
            hide_title_bar: whether hide the whole title bar.
            hide_button: whether hide part of buttons on title bar.
            disable_minimize_button: whether disable minimize button.
            disable_maximize_button: whether disable maximize button.
            border_type: border type of the window.
    
        Warning:
            This function is only works on Windows OS! And some parameters are
            useless on Windows 7/10!
    """
