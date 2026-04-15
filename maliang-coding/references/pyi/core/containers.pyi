"""
All containers.

There are two containers at the window level: ``Tk`` and ``Toplevel``. ``Tk`` is
generally used for the main window, while ``Toplevel`` is a pop-up window.

There is another container at the canvas level: ``Canvas``. ``Canvas`` is the
main container carrier.
"""

from __future__ import annotations
import abc
import functools
import sys
import tkinter
import tkinter.font
import traceback
from typing import TYPE_CHECKING
from typing_extensions import override
from ..theme import manager
from ..toolbox import enhanced, utility
from . import configs
from collections.abc import Callable
from typing import Any, Final, Literal
from typing_extensions import Self
from . import virtual

class Misc(abc.ABC):
    """
    An abstract miscellaneous class that implements some details.
    
        Currently, this class implements the ability to use the ``with`` statement
        for its subclasses for testing.
    """

    @abc.abstractmethod
    def destroy(self) -> None:
        """
        Destroy the object.
        """
    def __enter__(self) -> Self:
        ...
    def __exit__(self, *args, **kwargs) -> None:
        ...

class Tk(tkinter.Tk, Misc):
    """
    Main window.
    
        In general, there is only one main window. But after destroying it, another
        one can be created.
    
        Attributes:
            light (dict[str, str]): the color theme of light mode.
            dark (dict[str, str]): the color theme of dark mode.
    """

    light: dict[str, str]
    dark: dict[str, str]
    def __init__(self, size: tuple[int, int], position: tuple[int, int] | None, title: str | None, icon: str | enhanced.PhotoImage | None, **kwargs: Any) -> None:
        """
        Args:
                    size: size of the window.
                    position: position of the window, based on the upper left corner.
                        And negative numbers are based on the bottom right corner.
                    title: title of the window, default value is ``"tk"``.
                    icon: icon of the window, default value is the icon of tk.
                    kwargs: additional keyword arguments for ``tkinter.Tk``.
        """
    @functools.cached_property
    def ratios(self) -> tuple[float, float]:
        """
        The aspect zoom ratio of the container.
        """
    def theme(self, value: Literal['light', 'dark'], include_children: bool, include_canvases: bool) -> None:
        """
        Change the color theme of the window.
        
                Args:
                    value: theme name.
                    include_children: whether include its children, like ``Toplevel``.
                    include_canvases: whether include its canvases.
        """
    def geometry(self, size: tuple[int, int] | None, position: tuple[int, int] | None) -> tuple[int, int, int, int] | None:
        """
        Change the size and position of the window and return the current
                size and position of the window.
        
                Args:
                    size: the size of the window, if it is ``None``, does not change
                        anything.
                    position: the position of the window, if it is ``None``, does not
                        change anything.
        
                Returns:
                    The current size and position of the window if ``size`` or
                        ``position`` is not ``None``. Otherwise, returns ``None``.
        
                Note:
                    If you want to use ``tkinter.Tk.geometry``, please use
                        ``tkinter.Tk.wm_geometry`` instead.
        """
    def center(self, refer: tkinter.Misc | None) -> None:
        """
        Center the container.
        
                Args:
                    refer: The area of the reference widget, if it is None, means that
                        the reference area is the entire screen.
        """
    def icon(self, value: str | enhanced.PhotoImage) -> None:
        """
        Set the icon of the window.
        
                Args:
                    value: the icon.
        """
    def alpha(self, value: float | None) -> float | None:
        """
        Set or get the transparency of the window.
        
                Args:
                    value: the transparency of the window, range is ``0`` ~ ``1``.
        
                Returns:
                    The current transparency of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
        """
    def topmost(self, value: bool | None) -> bool | None:
        """
        Set or get whether the window is pinned or not.
        
                Args:
                    value: indicate whether the window is topmost.
        
                Returns:
                    The current topmost state of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
        """
    @_fixed_theme
    def fullscreen(self, value: bool | None) -> bool | None:
        """
        Set or get whether the window is full-screen.
        
                Args:
                    value: indicate whether the window is full-screen.
        
                Returns:
                    The current full-screen state of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
        
                Note:
                    The method should be called at the end of the code, or after some
                    time after the program has started.
        """
    @override
    def destroy(self) -> None:
        ...
    def at_exit(self, command: Callable[[], Any], ensure_destroy: bool) -> None:
        """
        Set a function that will be called when the window is closed.
        
                Args:
                    command: the function that will be called.
                    ensure_destroy: whether the window is guaranteed to be closed.
        """

class Toplevel(tkinter.Toplevel, Tk, Misc):
    """
    Toplevel window.
    
        It can be used as a pop-up window, or it can be customized to put anything
        you want to show.
    """

    def __init__(self, master: Tk | Toplevel | None, size: tuple[int, int], position: tuple[int, int] | None, title: str | None, icon: str | enhanced.PhotoImage | None, grab: bool, focus: bool, **kwargs: Any) -> None:
        """
        Args:
                    master: parent widget.
                    size: size of the window, default value is 960x540(px).
                    position: position of the window, default value indicates random.
                    title: title of window, default is the same as title of master.
                    icon: icon of the window, default is the same as title of master.
                    grab: whether to grab the window.
                    focus: whether direct input focus to this window.
                    kwargs: compatible with other parameters of class
                        ``tkinter.Toplevel``.
        """
    @override
    def destroy(self) -> None:
        ...

class Canvas(tkinter.Canvas, Misc):
    """
    Main contrainer: Canvas.
    
        The parent widget of all virtual widgets is ``Canvas``.
    
        Attributes:
            light (dict[str, str | int]): light theme colors.
            dark (dict[str, str | int]): dark theme colors.
    """

    light: dict[str, str | int]
    dark: dict[str, str | int]
    def __init__(self, master: Tk | Toplevel | Canvas | None, expand: Literal['', 'x', 'y', 'xy'], auto_zoom: bool, keep_ratio: Literal['min', 'max'] | None, free_anchor: bool, auto_update: bool | None, zoom_all_items: bool, **kwargs: Any) -> None:
        """
        Args:
                    master: parent widget.
                    expand: the mode of expand, ``x`` is horizontal, and ``y`` is
                        vertical.
                    auto_zoom: whether or not to scale its items automatically.
                    keep_ratio: the mode of aspect ratio, ``min`` follows the minimum
                        value, ``max`` follows the maximum value.
                    free_anchor: whether the anchor point is free-floating.
                    auto_update: whether the theme manager update it automatically.
                    zoom_all_items: whether or not to scale its allitems.
                    kwargs: compatible with other parameters of class
                        ``tkinter.Canvas``.
        """
    @functools.cached_property
    def ratios(self) -> tuple[float, float]:
        """
        The aspect zoom ratio of the widget.
        """
    def theme(self, value: Literal['light', 'dark']) -> None:
        """
        Change the color theme of the Canvas and its items.
        
                Args:
                    value: theme name.
        """
    def zoom(self) -> None:
        """
        Resize and position the ``Canvas`` based on the relevant parameters.
        
                This method only works for Canvas with Place layout.
        """
    @override
    def destroy(self) -> None:
        ...
    def clear(self) -> None:
        """
        Clear all things in the Canvas.
        """
    @override
    def create_text(self, x: float, y: float, *args, **kwargs) -> int:
        ...
    def on_motion(self, event: tkinter.Event, name: str) -> None:
        """
        Events to move the mouse.
        """
    def on_click(self, event: tkinter.Event, name: str) -> None:
        """
        Events to active the mouse.
        """
    def on_release(self, event: tkinter.Event, name: str) -> None:
        """
        Events to release the mouse.
        """
    def on_wheel(self, event: tkinter.Event, type_: bool | None) -> None:
        """
        Events to scroll the mouse wheel.
        """
    def on_key_press(self, event: tkinter.Event) -> None:
        """
        Events for typing.
        """
    def on_key_release(self, event: tkinter.Event) -> None:
        """
        Events for typing.
        """
    def register_event(self, name: str, add: bool | Literal['', '+'] | None) -> str:
        """
        Register a event to process.
        
                In general, you don't need to call this method, but when the event to
                be bound is not in the predefined event, you need to manually call the
                method once.
        
                Args:
                    name: the name of the event to register.
                    add: whether it is an attached call.
        """
    def hide_focus(self) -> None:
        """
        Hide the focus rectangle.
        """

def wrapper(tk: Tk, *args: Any, **kwargs: Any) -> Any:
    ...

def wrapper(*args: Any, **kwargs: Any) -> Any:
    ...

def toolwindow(self, value: bool | None) -> bool | None:
    """
    Set or get whether the window is tool-window.
    
                Args:
                    value: indicate whether the window is tool-window.
    
                Returns:
                    The current tool-window state of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
    
                Warning:
                    This method only works on Windows!
    """

def transparentcolor(self, value: str | None) -> str | None:
    """
    Set or get the penetration color of the window.
    
                Args:
                    value: the penetration color of the window.
    
                Returns:
                    The current penetration color of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
    
                Warning:
                    This method only works on Windows!
    """

def modified(self, value: bool | None) -> bool | None:
    """
    Set or get whether the window is modified.
    
                Args:
                    value: indicate whether the window is modified.
    
                Returns:
                    The current modified state of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
    
                Warning:
                    This method only works on macOS!
    """

def transparent(self, value: bool | None) -> bool | None:
    """
    Set or get whether the window is transparent.
    
                Args:
                    value: indicate whether the window is transparent.
    
                Returns:
                    The current transparent state of the window if ``value`` is not
                        ``None``. Otherwise, returns ``None``.
    
                Warning:
                    This method only works on macOS!
    """

def wrapper() -> None:
    ...

def handle_event(event: tkinter.Event) -> None:
    ...
