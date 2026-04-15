"""
Base and standard animation classes.

The animation base class can be inherited or called directly. Other standard
animation classes are best used by direct calls, rather than inheritance.
"""

from __future__ import annotations
from collections.abc import Sequence
from typing import TYPE_CHECKING, overload
from ..color import convert, rgb
from ..core import configs, containers
from . import controllers
import tkinter
from collections.abc import Callable
from typing import Any
from ..core import virtual

class Animation:
    """
    Base animation class.
    
        Attributes:
            command: callback function, which will be called once per frame.
            controller: a function that controls the animation process.
            end: end function, which is called once at the end of the animation.
            repeat: number of repetitions of the animation.
            repeat_delay: length of the delay before the animation repeats.
            derivation: whether the callback function is derivative.
    """

    def __init__(self, duration: int, command: Callable[[float], Any], controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        """
        Args:
                    duration: duration of the animation, in milliseconds.
                    command: callback function, which will be called once per frame.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
                    derivation: whether the callback function is derivative.
        """
    @property
    def active(self) -> bool:
        """
        The active state of the animation.
        """
    @property
    def count(self) -> int:
        """
        The number of loops remaining.
        """
    @overload
    def start(self) -> None:
        ...
    @overload
    def start(self, delay: int) -> str:
        ...
    def start(self, delay: int) -> str | None:
        """
        Start the animation.
        
                Args:
                    delay: length of the delay before the animation starts.
        
                Returns:
                    If ``delay`` is greater than ``0``, returns the identifier of the
                        scheduled task. Otherwise, returns ``None``.
        """
    @overload
    def stop(self) -> None:
        ...
    @overload
    def stop(self, delay: int) -> str:
        ...
    def stop(self, delay: int) -> str | None:
        """
        Stop the animation.
        
                Args:
                    delay: length of the delay before the animation stops.
        
                Returns:
                    If ``delay`` is greater than ``0``, returns the identifier of the
                        scheduled task. Otherwise, returns ``None``.
        """
    def skip(self, count: int) -> None:
        """
        Skip some loops.
        
                Args:
                    count: count of skipping.
        """

class MoveWindow(Animation):
    """
    Animation of moving the window.
    """

    def __init__(self, window: tkinter.Tk | tkinter.Toplevel | containers.Tk | containers.Toplevel, offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        """
        Args:
                    window: the window to be moved.
                    offset: relative offset of the coordinates.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
        """

class MoveTkWidget(Animation):
    """
    Animation of moving ``tkinter.Widget``.
    """

    def __init__(self, widget: tkinter.Widget, offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        """
        Args:
                    widget: the ``tkinter.Widget`` to be moved.
                    offset: relative offset of the coordinates.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
        
                Raises:
                    RuntimeError: if the widget is not laid out by Place.
        """

class MoveWidget(Animation):
    """
    Animation of moving ``virtual.Widget``.
    """

    @overload
    def __init__(self, widget: virtual.Widget, offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        ...
    @overload
    def __init__(self, widget: Sequence[virtual.Widget], offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        ...
    def __init__(self, widget: virtual.Widget | Sequence[virtual.Widget], offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        """
        Args:
                    widget: the ``virtual.Widget`` to be moved.
                    offset: relative offset of the coordinates.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
        """

class MoveElement(Animation):
    """
    Animation of moving ``virtual.Element``.
    """

    @overload
    def __init__(self, element: virtual.Element, offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        ...
    @overload
    def __init__(self, element: Sequence[virtual.Element], offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        ...
    def __init__(self, element: virtual.Element | Sequence[virtual.Element], offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        """
        Args:
                    element: the ``virtual.Element`` to be moved.
                    offset: relative offset of the coordinates.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
        """

class MoveItem(Animation):
    """
    Animation of moving a item of ``tkinter.Canvas``.
    """

    @overload
    def __init__(self, canvas: tkinter.Canvas | containers.Canvas, item: int, offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        ...
    @overload
    def __init__(self, canvas: tkinter.Canvas | containers.Canvas, item: Sequence[int], offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        ...
    def __init__(self, canvas: tkinter.Canvas | containers.Canvas, item: int | Sequence[int], offset: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int) -> None:
        """
        Args:
                    canvas: an instance of ``tkinter.Canvas`` that contains the item.
                    item: the item to be moved.
                    offset: relative offset of the coordinates.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
        """

class GradientTkWidget(Animation):
    """
    Animation of making the color of ``tkinter.Widget`` to be gradient.
    """

    @overload
    def __init__(self, widget: tkinter.Widget, parameter: str, colors: tuple[str, str], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        ...
    @overload
    def __init__(self, widget: Sequence[tkinter.Widget], parameter: str, colors: tuple[str, str], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        ...
    def __init__(self, widget: tkinter.Widget | Sequence[tkinter.Widget], parameter: str, colors: tuple[str, str], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        """
        Args:
                    widget: the ``tkinter.Widget`` whose color is to be gradient.
                    parameter: parameter name of widget that is to be modified in color.
                    colors: a tuple of the initial and ending colors.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
                    derivation: whether the callback function is derivative.
        
                Raises:
                    ValueError: if any color in ``colors`` is an empty string.
        """

class GradientItem(Animation):
    """
    Animation of making the color of canvas item to be gradient.
    """

    @overload
    def __init__(self, canvas: tkinter.Canvas | containers.Canvas, item: int, parameter: str, colors: tuple[str, str], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        ...
    @overload
    def __init__(self, canvas: tkinter.Canvas | containers.Canvas, item: Sequence[int], parameter: str, colors: tuple[str, str], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        ...
    def __init__(self, canvas: tkinter.Canvas | containers.Canvas, item: int | Sequence[int], parameter: str, colors: tuple[str, str], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        """
        Args:
                    canvas: an instance of ``tkinter.Canvas`` that contains the item.
                    item: item whose color is to be gradient.
                    parameter: parameter name of item that is to be modified in color.
                    colors: a tuple of the initial and ending colors.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
                    derivation: whether the callback function is derivative.
        
                Raises:
                    ValueError: if any color in ``colors`` is an empty string.
        """

class ScaleFontSize(Animation):
    """
    Animation of scaling the font size of ``virtual.Text``.
    """

    @overload
    def __init__(self, text: virtual.Text, sizes: float, duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        ...
    @overload
    def __init__(self, text: virtual.Text, sizes: tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        ...
    def __init__(self, text: virtual.Text, sizes: float | tuple[float, float], duration: int, controller: Callable[[float], float], end: Callable[[], Any] | None, fps: int, repeat: int, repeat_delay: int, derivation: bool) -> None:
        """
        Args:
                    text: an instance of ``virtual.Text`` that needs to be scaled.
                    sizes: a tuple of the initial and ending sizes or target font size.
                    duration: duration of the animation, in milliseconds.
                    controller: a function that controls the animation process.
                    end: end function, which is called once at the end of the animation.
                    fps: frame rate of the animation.
                    repeat: number of repetitions of the animation.
                    repeat_delay: length of the delay before the animation repeats.
                    derivation: whether the callback function is derivative.
        """

def callback(p) -> None:
    ...

def callback(p) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...

def command(p: float) -> None:
    ...
