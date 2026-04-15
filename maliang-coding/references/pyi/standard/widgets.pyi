"""
All standard ``Widget`` classes.
"""

from __future__ import annotations
import contextlib
import decimal
import itertools
import math
import warnings
from typing import TYPE_CHECKING
from typing_extensions import override
from ..animation import animations, controllers
from ..core import configs, virtual
from ..toolbox import utility
from . import features, images, shapes, styles, texts
from collections.abc import Callable
from typing import Any, Literal
from ..core import containers
from ..toolbox import enhanced

class Text(virtual.Widget):
    """
    Text widget, generally used to display plain text.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], wrap_length: int | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    wrap_length: limit the length of text, beyond which it will
                        automatically wrap.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> str:
        """
        Get the text of the widget.
        """
    def set(self, text: str) -> None:
        """
        Set the text of the widget.
        """

class Image(virtual.Widget):
    """
    Image widget, generally used to display normal still image.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> enhanced.PhotoImage:
        """
        Get the image of the widget.
        """
    def set(self, image: enhanced.PhotoImage | None) -> None:
        """
        Set the image of the widget.
        """

class Label(virtual.Widget):
    """
    Label widget, which is generally used to display key information.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> str:
        """
        Get the text of the widget.
        """
    def set(self, text: str) -> None:
        """
        Set the text of the widget.
        """

class Button(virtual.Widget):
    """
    Button widget, typically used to trigger a function.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], command: Callable | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    command: a function that is triggered when the button is pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> str:
        """
        Get the text of the widget.
        """
    def set(self, text: str) -> None:
        """
        Set the text of the widget.
        """

class Switch(virtual.Widget):
    """
    Switch widget, typically used to control the turning of a function on
        and off.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], length: int, default: bool | None, command: Callable[[bool], Any] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    length: length of the widget.
                    default: default value of the widget.
                    command: a function that is triggered when the switch is changed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> bool:
        """
        Get the state of the switch.
        """
    def set(self, value: bool, callback: bool) -> None:
        """
        Set the state of the switch.
        """

class InputBox(virtual.Widget):
    """
    Input box widget, generally used to enter certain information on a single
        line.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, align: Literal['left', 'right', 'center'], placeholder: str, show: str | None, ignore: tuple[str, ...], limit: int, limit_width: int, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    align: align mode of the text.
                    show: display a value that obscures the original content.
                    ignore: ignore the input of some characters.
                    placeholder: a placeholder for the prompt.
                    limit: limit on the number of characters.
                    limit_width: limit on the width of characters.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> str:
        """
        Get the value of the Entry.
        """
    def set(self, value: str) -> bool:
        """
        Set the text value of the Entry.
        """
    def insert(self, index: int, value: str) -> bool:
        """
        Insert.
        """
    def append(self, value: str) -> bool:
        """
        Append text to Entry.
        """
    def remove(self, start: int, end: int | None) -> int:
        """
        Remove.
        """
    def pop(self, index: int) -> str:
        """
        Delete a specified amount of text.
        """
    def clear(self) -> None:
        """
        Clear the text value of the Entry.
        """
    @override
    def update(self, state: str | None, gradient_animation: bool | None, nested: bool) -> None:
        """
        Update the widget.
        
                Args:
                    state: state of the widget.
                    gradient_animation: whether use gradient animation.
                    nested: whether nested.
        """

class CheckBox(virtual.Widget):
    """
    Checkbox button widget, generally used to check some options.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], length: int, default: bool | None, command: Callable[[bool], Any] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    length: length of the widget.
                    default: default state of the widget.
                    command: a function that is triggered when the state of check button
                        is on.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> bool:
        """
        Get the state of the check button.
        """
    def set(self, value: bool, callback: bool) -> None:
        """
        Set the state of the check button.
        """

class ToggleButton(virtual.Widget):
    """
    A button that can display information and switch statuses.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], default: bool | None, command: Callable[[bool], Any] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    default: default state of the widget.
                    command: a function that is triggered when the state of check button
                        is on.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> bool:
        """
        Get the state of the check button.
        """
    def set(self, value: bool, callback: bool) -> None:
        """
        Set the state of the switch.
        """

class RadioBox(virtual.Widget):
    """
    Radio button widget, generally used to select one of several options.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], length: int, default: bool | None, command: Callable[[int], Any] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    length: length of the widget.
                    default: default state of the widget.
                    command: a function that is triggered when the state of radio button
                        is on.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> bool:
        """
        Get the state of the radio button.
        """
    def set(self, value: bool, callback: bool) -> None:
        """
        Set the state of the radio button.
        """
    def group(self, *radio_boxes: RadioBox) -> None:
        """
        Combine other radio boxes.
        
                Args:
                    radio_boxes: other radio boxes.
        """

class ProgressBar(virtual.Widget):
    """
    Progress bar widget, typically used to show the progress of an event.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int], default: float | None, command: Callable[[float], Any] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    default: default value of the widget
                    command: a function that is triggered when the progress of progress
                        bar is 100%.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> float:
        """
        Get the progress of the progress bar.
        """
    def set(self, value: float, callback: bool) -> None:
        """
        Set the progress of the progress bar.
        """

class UnderlineButton(virtual.Widget):
    """
    Underline button, generally used to display web links.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], command: Callable | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    command: a function that is triggered when the underline button is
                        pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """

class HighlightButton(virtual.Widget):
    """
    Highlight button, no outline, which added a highlight effect.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], command: Callable | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    command: a function that is triggered when the hightlight button is pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """

class IconButton(virtual.Widget):
    """
    A button with an icon on the left side.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: str, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], command: Callable | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    command: a function that is triggered when the button is pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> str:
        """
        Get the text of the widget.
        """
    def set(self, text: str) -> None:
        """
        Set the text of the widget.
        """

class Slider(virtual.Widget):
    """
    A slider for visually resizing values.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int], default: float | None, command: Callable[[float], Any] | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    default: default value of the widget.
                    command: a function that is triggered when the button is pressed.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> float:
        """
        Get the value of the slider.
        """
    def set(self, value: float, callback: bool) -> None:
        """
        Set the value of the slider.
        """

class SegmentedButton(virtual.Widget):
    """
    A segmented button that can be used to toggle between multiple states.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], sizes: tuple[tuple[int, int], ...], text: tuple[str, ...], family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], default: int | None, command: Callable[[int | None], Any] | None, image: tuple[enhanced.PhotoImage | None, ...], layout: Literal['horizontal', 'vertical'], anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    sizes: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    default: default value of the widget.
                    command: a function that is triggered when the button is pressed.
                    image: image of the widget.
                    layout: layout mode of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> int | None:
        """
        Get the index of the child toggle button with a value of True. If
                not, None is returned.
        """
    def set(self, value: int | None, callback: bool) -> None:
        """
        Activate the child toggle button for the specified index.
        """

class SpinBox(virtual.Widget):
    """
    A widget that makes it easy to enter numeric type data.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, format_spec: str, step: float, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, align: Literal['left', 'right', 'center'], placeholder: str, show: str | None, limit: int, default: str | None, command: Callable[[bool], Any] | None, image: enhanced.PhotoImage | None, anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    format_spec: format of value.
                    step: value of each change.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    align: align mode of the text.
                    show: display a value that obscures the original content.
                    placeholder: a placeholder for the prompt.
                    limit: limit on the number of characters.
                    default: default value of the widget.
                    command: a function that is triggered when the button is pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def change(self, up: bool) -> None:
        """
        Try change the current value.
        """
    def get(self) -> str:
        """
        Get the value of the Entry.
        """
    def set(self, value: str) -> None:
        """
        Set the text value of the Entry.
        """
    def append(self, value: str) -> None:
        """
        Append text to Entry.
        """
    def delete(self, count: int) -> None:
        """
        Delete a specified amount of text.
        """
    def clear(self) -> None:
        """
        Clear the text value of the Entry.
        """

class OptionButton(virtual.Widget):
    """
    A button that has many options to choose.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: tuple[str, ...], family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], default: int | None, command: Callable[[int | None], Any] | None, image: tuple[enhanced.PhotoImage | None, ...], anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], align: Literal['up', 'center', 'down'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    default: default value of the widget.
                    command: a function that is triggered when the button is pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    align: align of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> int | None:
        """
        Get the index of the child toggle button with a value of True. If
                not, None is returned.
        """
    def set(self, value: int | None, callback: bool) -> None:
        """
        Activate the child toggle button for the specified index.
        """

class ComboBox(virtual.Widget):
    """
    An input box that can provide several options.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int] | None, text: tuple[str, ...], family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], default: int | None, command: Callable[[int | None], Any] | None, image: tuple[enhanced.PhotoImage | None, ...], anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], align: Literal['up', 'down'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    text: text of the widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    default: default value of the widget.
                    command: a function that is triggered when the button is pressed.
                    image: image of the widget.
                    anchor: anchor of the widget.
                    align: align of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> int | None:
        """
        Get the index of the child toggle button with a value of True. If
                not, None is returned.
        """
    def set(self, value: int | None, callback: bool) -> None:
        """
        Activate the child toggle button for the specified index.
        """

class Spinner(virtual.Widget):
    """
    Spinners visually communicate that something is processing.
    """

    def __init__(self, master: containers.Canvas | virtual.Widget, position: tuple[int, int], size: tuple[int, int], default: float | None, command: Callable[[float], Any] | None, widths: tuple[int, int] | None, mode: Literal['determinate', 'indeterminate'], anchor: Literal['n', 'e', 'w', 's', 'nw', 'ne', 'sw', 'se', 'center'], capture_events: bool | None, gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    master: parent canvas.
                    position: position of the widget.
                    size: size of the widget.
                    default: default value of the widget.
                    command: a function that is triggered when the progress of progress
                        bar is 100%.
                    widths: width of the outside ring and inside ring.
                    mode: mode of the Spinner.
                    anchor: anchor of the widget.
                    capture_events: whether detect another widget under the widget.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> float:
        """
        Get the progress of the Spinner.
        """
    def set(self, value: float, callback: bool) -> None:
        """
        Set the progress of the Spinner.
        """
    @override
    def destroy(self) -> None:
        """
        Destroy the widget.
        """

class Tooltip(virtual.Widget):
    """
    A tooltip that can display additional information.
    """

    def __init__(self, widget: virtual.Widget, size: tuple[int, int] | None, text: str, align: Literal['up', 'down', 'right', 'left', 'center'], padding: int, family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, justify: Literal['left', 'center', 'right'], gradient_animation: bool | None, auto_update: bool | None, style: type[virtual.Style] | None) -> None:
        """
        Args:
                    widget: the associated widget.
                    size: size of the widget.
                    text: text of the widget.
                    align: align mode of the tooltip.
                    padding: extra padding between tooltip and the associated widget.
                    family: font family.
                    fontsize: font size.
                    weight: weight of the text.
                    slant: slant of the text.
                    underline: whether the text is underline.
                    overstrike: whether the text is overstrike.
                    justify: justify mode of the text.
                    gradient_animation: whether enable gradient_animation.
                    auto_update: whether the theme manager update it automatically.
                    style: style of the widget.
        """
    def get(self) -> str:
        """
        Get the text of the widget.
        """
    def set(self, text: str) -> None:
        """
        Set the text of the widget.
        """
