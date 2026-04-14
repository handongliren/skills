"""All standard dialog classes."""

from __future__ import annotations
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import warnings
from collections.abc import Callable, Sequence
from typing import Any, Literal

class TkMessage:
    """Message pop-up."""

    def __init__(self, message: str | None, detail: str | None, title: str | None, icon: Literal['error', 'info', 'question', 'warning'], option: Literal['abortretryignore', 'ok', 'okcancel', 'retrycancel', 'yesno', 'yesnocancel'], default: Literal['abort', 'retry', 'ignore', 'ok', 'cancel', 'yes', 'no'] | None, master: tkinter.Tk | None, command: Callable[[Literal['abort', 'retry', 'ignore', 'ok', 'cancel', 'yes', 'no']], Any] | None) -> None: ...

class TkColorChooser:
    """Color chooser pop-up."""

    def __init__(self, title: str | None, color: str | None, master: tkinter.Tk | None, command: Callable[[str], Any] | None) -> None: ...

class TkFontChooser:
    """Font chooser pop-up."""

    def __init__(self, title: str | None, font: str | None, master: tkinter.Tk | None, command: Callable[[str], Any] | None) -> None: ...

class _TkFileChooser:
    """File chooser pop-up."""

    def __init__(self, is_dir: bool, mode: Literal['save', 'open'], title: str | None, initialdir: str | None, initialfile: str | None, filetypes: Sequence[tuple[str, str]] | None, defaultextension: str | None, multiple: bool, master: tkinter.Tk | None, command: Callable[[str | tuple[str, ...]], Any] | None) -> None: ...
