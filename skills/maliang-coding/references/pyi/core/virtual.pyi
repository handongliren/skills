"""
All virtual classes.

The ``virtual.Widget`` consists of five parts, which are ``Shape``, ``Text``,
``Image``, ``Style`` and ``Feature``. In addition, they can be nested within
each other.

Where ``Feature`` is the function of widgets, ``Style`` control the color of the
widget, and each widget can be bound to up to one ``Feature`` and one ``Style``,
but in terms of appearance, there is no limit to the number of ``Shape``,
``Text``, and ``Image``.

``Shape``, ``Text``, and ``Image`` are all appearance elements that inherit from
abstract base class ``Elements``.
"""

from __future__ import annotations
import abc
import copy
import math
import re
import tkinter
import tkinter.font
import traceback
import types
import warnings
from typing import TYPE_CHECKING
from typing_extensions import override
from ..animation import animations
from ..color import convert, rgb
from ..theme import manager
from . import configs
from collections.abc import Callable
from typing import Any, Literal
from typing_extensions import Self
from ..toolbox import enhanced
from . import containers

class Element(abc.ABC):
    """
    The basic visible part of a ``virtual.Widget``.
    """

    def __init__(self, widget: Widget, position: tuple[int, int], size: tuple[int, int] | None, name: str | None, gradient_animation: bool | None, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    position: position relative to its widgets.
                    size: size of element.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for element.
        """
    def move(self, dx: float, dy: float) -> None:
        """
        Move the ``Element``.
        
                Args:
                    dx: x-coordinate offset.
                    dy: y-coordinate offset.
        """
    def moveto(self, x: float, y: float) -> None:
        """
        Move the ``Element`` to a certain position.
        
                Args:
                    x: x-coordinate of the target location.
                    y: y-coordinate of the target location.
        """
    def destroy(self) -> None:
        """
        Destroy the ``Element``.
        """
    def center(self) -> tuple[float, float]:
        """
        Return the geometric center of the ``Element``.
        """
    def region(self) -> tuple[int, int, int, int]:
        """
        Return the decision region of the ``Element``.
        """
    def detect(self, x: float, y: float) -> bool:
        """
        Detect whether the specified coordinates are within ``Element``.
        
                Args:
                    x: x-coordinate of the location to be detected.
                    y: y-coordinate of the location to be detected.
        """
    def update(self, state: str | None, gradient_animation: bool) -> None:
        """
        Update the style of the ``Element`` to the corresponding state.
        
                Args:
                    state: the state of the ``Element``.
                    gradient_animation: whether use gradient animation.
        """
    def configure(self, style: dict[str, str], gradient_animation: bool) -> None:
        """
        Configure properties of ``Element`` and update them immediately.
        
                Args:
                    style: style data.
                    gradient_animation: whether use gradient animation.
        """
    def forget(self, value: bool, gradient_animation: bool) -> None:
        """
        Let the element to forget.
        
                Args:
                    value: whether to forget.
                    gradient_animation: whether use gradient animation.
        """
    def zoom(self, ratios: tuple[float, float], zoom_position: bool, zoom_size: bool) -> None:
        """
        Zoom the ``Element``.
        
                Args:
                    ratios: ratios of zooming.
                    zoom_position: whether or not to zoom the location of the element.
                    zoom_size: whether or not to zoom the size of the element.
        """
    @abc.abstractmethod
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @abc.abstractmethod
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        
                Args:
                    size: new size of the element.
                    position: new position of the element.
        """

class Shape(Element):
    """
    The Shape of a ``Widget``.
    """

    @override
    def zoom(self, ratios: tuple[float, float], zoom_position: bool, zoom_size: bool) -> None:
        """
        Scale the shape.
        
                Args:
                    ratios: ratios of zooming.
                    zoom_position: whether or not to zoom the location of the shape.
                    zoom_size: whether or not to zoom the size of the shape.
        """

class Text(Element):
    """
    The Text of a ``Widget``.
    """

    def __init__(self, widget: Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, text: str, limit: int, show: str | None, placeholder: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    text: text value.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the font.
                    slant: slant of the font.
                    underline: whether text is underline.
                    overstrike: whether text is overstrike.
                    limit: limit on the number of characters.
                    show: display a value that obscures the original content.
                    placeholder: a placeholder for the prompt.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    def region(self) -> tuple[int, int, int, int]:
        """
        Return the decision region of the ``Text``.
        """
    @override
    def zoom(self, ratios: tuple[float, float], zoom_position: bool, zoom_size: bool) -> None:
        """
        Scale the text.
        
                Args:
                    ratios: ratios of zooming.
                    zoom_position: whether or not to zoom the location of the text.
                    zoom_size: whether or not to zoom the size of the text.
        """

class Image(Element):
    """
    The Image of a ``Widget``.
    """

    def __init__(self, widget: Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, image: enhanced.PhotoImage | None, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
        """
        Args:
                    widget: parent widget.
                    relative_position: position relative to its widgets.
                    size: size of element.
                    image: image object of the element.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    def region(self) -> tuple[int, int, int, int]:
        """
        Return the decision region of the ``Image``.
        """
    @override
    def zoom(self, ratios: tuple[float, float], zoom_position: bool, zoom_size: bool) -> None:
        """
        Scale the image.
        
                Args:
                    ratios: ratios of zooming.
                    zoom_position: whether or not to zoom the location of the image.
                    zoom_size: whether or not to zoom the size of the image.
        
                Raises:
                    RuntimeError: if the image is empty.
        """

class Style:
    """
    The styles of a ``Widget``.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]): style data of light theme.
            dark (dict[str, dict[str, dict[str, str]]]): style data of dark theme.
    """

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    def __init__(self, widget: Widget, auto_update: bool | None) -> None:
        """
        Args:
                    widget: parent widget.
                    auto_update: whether the theme manager update it automatically.
        """
    def __getitem__(self, key: Element | str | int) -> dict[str, dict[str, str]]:
        ...
    def get_disabled_style(self, element: Element) -> dict[str, str]:
        """
        Get the style data of disabled state.
        
                Args:
                    element: element that style to be calculated.
        
                Returns:
                    style data of disabled state.
        """
    def init(self, key: Element | str | int, theme: Literal['light', 'dark'] | None) -> None:
        """
        Initialize some style of an element.
        
                Args:
                    key: the object related to the key.
                    theme: the theme name, ``None`` indicates both.
        """
    def get(self, theme: Literal['light', 'dark'] | None) -> dict[str, dict[str, dict[str, str]]]:
        """
        Return the style of the widget.
        
                Args:
                    theme: the theme of the widget, ``None`` indicates the current
                        theme.
        
                Returns:
                    the style of the widget.
        """
    def reset(self, theme: Literal['light', 'dark'] | None) -> None:
        """
        Reset the style of the widget and update.
        
                Args:
                    theme: the theme to be reset, ``None`` indicates both.
        """
    def detach(self) -> Self:
        """
        Detach the style data from the class data.
        """
    def set(self) -> None:
        """
        Set the style of the widget.
        """

class Feature:
    """
    The features of a ``Widget``.
    """

    def __init__(self, widget: Widget) -> None:
        """
        Args:
                    widget: parent widget.
        """
    def get_method(self, name: str) -> Callable:
        """
        Return method by name.
        
                Args:
                    name: name of the method.
        
                Returns:
                    method.
        """

class Widget:
    """
    Base Widget Class.
    
        ``Widget`` = ``Element`` + ``Style`` + ``Feature``
    """

    def __init__(self, master: containers.Canvas | Widget, position: tuple[int, int], size: tuple[int, int] | None, anchor: Literal['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_resize: bool | None, auto_update: bool | None, style: type[Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    anchor: layout anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable animation.
                    auto_resize: whether to automatically resize after modifying the
                        content of the widget.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    @property
    def elements(self) -> tuple[Element, ...]:
        """
        All elements of the widget.
        """
    @property
    def children(self) -> tuple[Widget, ...]:
        """
        All child widgets of the widget.
        """
    @property
    def nested(self) -> bool:
        """
        Whether the widget is a nested widget.
        """
    @property
    def offset(self) -> tuple[float, float]:
        """
        The offset of the anchor relative to "nw".
        """
    def register_elements(self, *elements: Element) -> None:
        """
        Register elements to the widget.
        
                Args:
                    elements: elements to be registered.
        """
    def deregister_elements(self, *elements: Element) -> None:
        """
        Deregister a element from the widget.
        
                Args:
                    elements: elements to be deregistered.
        """
    def update(self, state: str | None, gradient_animation: bool | None, nested: bool) -> None:
        """
        Update the widget.
        
                Args:
                    state: state of the widget.
                    gradient_animation: whether use gradient animation.
                    nested: whether nested.
        """
    def bind_on_update(self, command: Callable[[str, bool], Any]) -> None:
        """
        Bind an extra function to the widget on update.
        
                This extra function has two positional arguments, both of which are
                arguments to the method ``update``. And this extra function will be
                called when the widget is updated (whether it's automatically updated
                or manually updated).
        
                Args:
                    command: the extra function that is bound.
        """
    def unbind_on_update(self, command: Callable[[str, bool], Any]) -> None:
        """
        Unbind an extra function to the widget on update.
        
                Args:
                    command: the extra function that is bound.
        """
    def bind(self, sequence: str, command: Callable[[tkinter.Event], Any], add: bool | Literal['', '+'] | None, auto_detect: bool) -> None:
        """
        Bind to this widget at event sequence a call to function command.
        
                Args:
                    sequence: event name
                    command: callback function
                    add: if True, original callback function will not be overwritten
                    auto_detect: Automatically determine whether to execute binding
                        events based on the method ``detect``
        """
    def unbind(self, sequence: str, command: Callable[[tkinter.Event], Any]) -> None:
        """
        Unbind for this widget the event sequence.
        
                Args:
                    sequence: event name.
                    command: callback function.
        """
    def generate_event(self, sequence: str, event: tkinter.Event | None, **kwargs: Any) -> None:
        """
        Generate an event sequence. Additional keyword arguments specify
                parameter of the event.
        
                Args:
                    sequence: event name.
                    event: event.
                    kwargs: attr of event.
        """
    def disable(self, value: bool) -> None:
        """
        Disable the widget.
        
                Args:
                    value: whether to disable.
        """
    def forget(self, value: bool) -> None:
        """
        Let all elements of the widget to forget.
        
                Args:
                    value: whether to forget the widget.
        """
    def lift(self) -> None:
        """
        Lift the widget to the top.
        """
    def move(self, dx: float, dy: float) -> None:
        """
        Move the widget.
        
                Args:
                    dx: x-coordinate offset.
                    dy: y-coordinate offset.
        """
    def moveto(self, x: float, y: float) -> None:
        """
        Move the Widget to a certain position.
        
                Args:
                    x: x-coordinate of the target location.
                    y: y-coordinate of the target location.
        """
    def destroy(self) -> None:
        """
        Destroy the widget.
        """
    def exists(self) -> bool:
        """
        Check if the widget exists.
        """
    def region(self) -> tuple[int, int, int, int]:
        """
        Return the decision region of the ``Widget``.
        """
    def detect(self, x: float, y: float) -> bool:
        """
        Detect whether the specified coordinates are within the ``Widget``.
        
                Args:
                    x: x-coordinate of the location to be detected.
                    y: y-coordinate of the location to be detected.
        
                Returns:
                    whether the location is within the widget.
        """
    def center(self) -> tuple[int, int]:
        """
        Return the center of the widget.
        """
    def zoom(self, ratios: tuple[float, float] | None, zoom_position: bool, zoom_size: bool) -> None:
        """
        Zoom widget ifself.
        
                Args:
                    ratios: ratios of zooming.
                    zoom_position: whether or not to zoom the location of the widget.
                    zoom_size: whether or not to zoom the size of the widget.
        """
    def resize(self, size: tuple[float, float] | None) -> None:
        """
        Resize the widget.
        
                Args:
                    size: new size for the widget.
        """

def wrapper(event: tkinter.Event) -> Any:
    ...

def wrapper(event: tkinter.Event) -> Any:
    ...
