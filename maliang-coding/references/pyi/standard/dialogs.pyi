"""
All standard dialog classes.
"""

from __future__ import annotations
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import warnings
from typing import TYPE_CHECKING
from collections.abc import Callable, Sequence
from typing import Any, Literal

class TkMessage:
    """
    Message pop-up.
    """

    def __init__(self, message: str | None, detail: str | None, title: str | None, icon: Literal['error', 'info', 'question', 'warning'], option: Literal['abortretryignore', 'ok', 'okcancel', 'retrycancel', 'yesno', 'yesnocancel'], default: Literal['abort', 'retry', 'ignore', 'ok', 'cancel', 'yes', 'no'] | None, master: tkinter.Tk | None, command: Callable[[Literal['abort', 'retry', 'ignore', 'ok', 'cancel', 'yes', 'no']], Any] | None) -> None:
        """
        Args:
                    message: message.
                    detail: detail message.
                    title: title of the window.
                    icon: icon.
                    option: type of the message pop-up.
                    default: button where the focus is, default is the leftmost one.
                    master: parent widget.
                    command: callback function.
        """

class TkColorChooser:
    """
    Color chooser pop-up.
    """

    def __init__(self, title: str | None, color: str | None, master: tkinter.Tk | None, command: Callable[[str], Any] | None) -> None:
        """
        Args:
                    title: title of the window.
                    color: default color.
                    master: parent widget of the window.
                    command: callback function.
        """

class TkFontChooser:
    """
    Font chooser pop-up.
    """

    def __init__(self, title: str | None, font: str | None, master: tkinter.Tk | None, command: Callable[[str], Any] | None) -> None:
        """
        Args:
                    title: title of the window.
                    font: default font.
                    master: parent widget of the window.
                    command: callback function.
        """

class _TkFileChooser:
    """
    File chooser pop-up.
    """

    def __init__(self, is_dir: bool, mode: Literal['save', 'open'], title: str | None, initialdir: str | None, initialfile: str | None, filetypes: Sequence[tuple[str, str]] | None, defaultextension: str | None, multiple: bool, master: tkinter.Tk | None, command: Callable[[str | tuple[str, ...]], Any] | None) -> None:
        """
        Args:
                    is_dir: whether to select a directory.
                    mode: whether to save or open a file.
                    title: title of the window.
                    initialdir: initial directory.
                    initialfile: initial file.
                    filetypes: file types to filter.
                        (e.g., ``[("Text Files", "*.txt"), ("All Files", "*.*")]``)
                    defaultextension: default file extension.
                    multiple: whether to allow multiple file selection.
                    master: parent widget of the window.
                    command: callback function.
        """
