"""APIs for Matplotlib"""

from __future__ import annotations
import inspect
import tkinter
import typing
import matplotlib
import matplotlib.backends._backend_tk
import matplotlib.backends.backend_tkagg
import matplotlib.figure
import mpl_toolkits.mplot3d
import typing_extensions
from maliang.core import configs
from maliang.theme import manager
from . import constants

class FigureCanvas(tkinter.Canvas, matplotlib.backends.backend_tkagg.FigureCanvasTkAgg):
    """A canvas for interface of `matplotlib`"""

    def __init__(self, master: tkinter.Misc, figure: matplotlib.figure.Figure, *args, **kwargs) -> None: ...
    def theme(self, theme: typing.Literal['light', 'dark']) -> None: ...
    @typing_extensions.override
    def destroy(self) -> None: ...

class FigureToolbar(matplotlib.backends._backend_tk.NavigationToolbar2Tk):
    """An interface class for the matplotlib navigation cursor"""

    def __init__(self, master: tkinter.Misc | FigureCanvas, figure_canvas: FigureCanvas | None, pack_toolbar: bool, **kwargs) -> None: ...
    def theme(self, theme: typing.Literal['light', 'dark']) -> None: ...
    @typing_extensions.override
    def destroy(self) -> None: ...

def set_mpl_default_theme(theme: typing.Literal['light', 'dark'], apply_font: bool) -> None: ...
