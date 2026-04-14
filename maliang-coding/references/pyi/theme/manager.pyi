"""Support for theme.

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
from collections.abc import Callable
from typing import TYPE_CHECKING, Any, Literal
from ..core import configs
from ..toolbox import utility
import pywinstyles
import hPyT
import win32material
import tkinter
import darkdetect
import darkdetect._windows_detect
import darkdetect

def set_color_mode(mode: Literal['system', 'dark', 'light']) -> None: ...

def get_color_mode() -> Literal['dark', 'light']: ...

def register_event(func: Callable[..., Any], *args: Any) -> None: ...

def remove_event(func: Callable[..., Any]) -> None: ...

def apply_file_dnd(window: tkinter.Tk, command: Callable[[str], Any]) -> None: ...

def apply_theme(window: tkinter.Tk, theme: Literal['mica', 'acrylic', 'acrylic2', 'aero', 'transparent', 'optimised', 'win7', 'inverse', 'native', 'popup', 'dark', 'normal']) -> None: ...

def customize_window(window: tkinter.Tk, border_color: str | None, header_color: str | None, title_color: str | None, hide_title_bar: bool | None, hide_button: Literal['all', 'maxmin', 'none'] | None, disable_minimize_button: bool | None, disable_maximize_button: bool | None, border_type: Literal['rectangular', 'smallround', 'round'] | None) -> None: ...
