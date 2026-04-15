"""
APIs for tksheet
"""

from __future__ import annotations
import typing
import tksheet
from maliang.theme import manager
from . import constants

class TkTable(tksheet.Sheet):
    """
    A tkinter widget for displaying a table.
    """

    def __init__(self, *args, **kwargs) -> None:
        ...
    def theme(self, value: typing.Literal['light', 'dark']) -> None:
        """
        Change the color theme of the table.
        
                * `value`: theme name
        """
