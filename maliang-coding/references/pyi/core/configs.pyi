"""All global configuration options.

Some options are read-only, but most of them can be changed, and once changed,
they will take effect globally for the program. Some changes take effect
immediately, but some need to take effect when the relevant option is invoked.
"""

from __future__ import annotations
import ctypes
import math
import platform
import sys
import tkinter
from typing import TYPE_CHECKING
from typing import Any, Final, Literal

class _DefaultRootDescriptor:
    """A simple descriptor for ``tkinter._default_root``."""

    def __get__(self, *args: Any, **kwargs: Any) -> tkinter.Tk: ...

class Env:
    """Configurations for default environment values.

    Attributes:
        system (str): The system of environment, such as ``"Windows10"``,
            ``"Windows11"``, ``"Linux"``, ``"Darwin"`` (macOS).
        theme (Literal["light", "dark"]): The theme of the application.
        gradient_animation (bool): Whether to enable gradient animation for
            widgets that support it by default.
        auto_update (bool): Whether to check for updates automatically on
            startup.
        root (tkinter.Tk): The current default root window. It is READ-ONLY."""

    system: str
    theme: Literal['light', 'dark']
    gradient_animation: bool
    auto_update: bool
    root = _DefaultRootDescriptor()
    @classmethod
    def reset(cls) -> None: ...
    @staticmethod
    def get_default_system() -> str: ...

class Font:
    """Configurations for default font.
    
    Attributes:
        family (str): The default font family.
        size (int): The default font size, negative value means size in pixels."""

    family: str
    size: int
    @classmethod
    def reset(cls) -> None: ...
    @staticmethod
    def get_default_family() -> str: ...

class Constant:
    """All Constants."""

    GOLDEN_RATIO: Final[float]
    PREDEFINED_EVENTS: Final[tuple[str, ...]]
    PREDEFINED_VIRTUAL_EVENTS: Final[tuple[str, ...]]

def reset() -> None: ...
