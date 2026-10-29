"""
All standard ``Text`` classes.
"""

from __future__ import annotations
import bisect
import itertools
import tkinter.font
import warnings
from typing import TYPE_CHECKING
from typing_extensions import override
from ..core import virtual
from typing import Any, Literal
from ..core import containers

class _CanvasTextProxy:
    def __init__(self, canvas: containers.Canvas, tag_or_id: str | int) -> None:
        ...
    def length(self) -> int:
        """
        Length.
        """
    def get(self) -> str:
        """
        Get.
        """
    def set(self, value: str, show: str | None) -> None:
        """
        Set.
        """
    def insert(self, index: int, value: str, show: str | None) -> None:
        """
        Insert.
        """
    def append(self, value: str, show: str | None) -> None:
        """
        Append.
        """
    def remove(self, start: int, end: int | None) -> None:
        """
        Remove.
        """
    def pop(self, index: int) -> str:
        """
        Pop.
        """
    def clear(self) -> None:
        """
        Clear.
        """
    def select_get(self) -> tuple[int, int] | None:
        """
        select get.
        """
    def select_set(self, start: int, end: int | None) -> None:
        """
        select set.
        """
    def select_all(self) -> None:
        """
        select all.
        """
    def select_clear(self) -> None:
        """
        select clear.
        """
    def cursor_get(self) -> int | None:
        """
        cursor get.
        """
    def cursor_set(self, index: int) -> None:
        """
        cursor set.
        """
    def cursor_find(self, x: int) -> int:
        """
        cursor find.
        """

class Information(virtual.Text):
    """
    General information text.
    """

    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """
    def get(self) -> str:
        """
        Get the value of ``Text``.
        """
    def set(self, text: str) -> None:
        """
        Set the value of ``Text``.
        """
    def append(self, text: str) -> None:
        """
        Append value to the value of ``Text``.
        """
    def delete(self, num: int) -> None:
        """
        Remove a portion of the ``Text`` value from the trail.
        """
    def clear(self) -> None:
        """
        Clear the value of ``Text``.
        """

class SingleLineText(virtual.Text):
    """
    Single-line editable text.
    """

    def __init__(self, widget: virtual.Widget, relative_position: tuple[int, int], size: tuple[int, int] | None, text: str, ignore: tuple[str, ...] | str, limit: int, limit_width: int, show: str | None, placeholder: str, align: Literal['left', 'center', 'right'], family: str | None, fontsize: int | None, weight: Literal['normal', 'bold'], slant: Literal['roman', 'italic'], underline: bool, overstrike: bool, name: str | None, gradient_animation: bool, **kwargs: Any) -> None:
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
                    align: align mode of the text.
                    ignore: ignore the input of some characters.
                    limit: limit on the number of characters.
                    limit_width: limit on the width of characters.
                    show: display a value that obscures the original content.
                    placeholder: a placeholder for the prompt.
                    name: name of element.
                    gradient_animation: whether use animation to change color.
                    kwargs: extra parameters for CanvasItem.
        """
    @override
    def display(self) -> None:
        """
        Display the ``Element`` on a ``Canvas``.
        """
    @override
    def coords(self, size: tuple[float, float] | None, position: tuple[float, float] | None) -> None:
        """
        Resize the ``Element``.
        """
    def get(self) -> str:
        """
        Get text of the element.
        """
    def set(self, value: str) -> bool:
        """
        Set text of the element.
        """
    def insert(self, index: int, value: str) -> bool:
        """
        Insert text to the location of the specified index.
        """
    def append(self, value: str) -> bool:
        """
        Add some characters to the text cursor.
        """
    def remove(self, start: int, end: int | None) -> None:
        """
        Remove text within the specified index range.
        """
    def pop(self, index: int) -> str:
        """
        Delete a character at the text cursor.
        """
    def clear(self) -> None:
        """
        Clear.
        """
    def cursor_move(self, count: int) -> None:
        """
        Move the index position of the text cursor.
        """
    def cursor_move_to(self, count: int) -> None:
        """
        Move the index position of the text cursor to a certain index.
        """
