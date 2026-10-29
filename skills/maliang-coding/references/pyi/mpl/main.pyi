"""
APIs for Matplotlib
"""

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
    """
    A canvas for interface of `matplotlib`
    """

    def __init__(self, master: tkinter.Misc, figure: matplotlib.figure.Figure, *args, **kwargs) -> None:
        """
        * `master`: parent widget
                * `figure`: a `Figure` object from `matplotlib`
        """
    def theme(self, theme: typing.Literal['light', 'dark']) -> None:
        """
        Change the color theme of the Figure.
        
                * `theme`: the theme name
        """
    @typing_extensions.override
    def destroy(self) -> None:
        ...

class FigureToolbar(matplotlib.backends._backend_tk.NavigationToolbar2Tk):
    """
    An interface class for the matplotlib navigation cursor
    """

    def __init__(self, master: tkinter.Misc | FigureCanvas, figure_canvas: FigureCanvas | None, pack_toolbar: bool, **kwargs) -> None:
        """
        * `master`: parent widget
                * `figure_canvas`: the figure canvas on which to operate
                * `pack_toolbar`: if True, add the toolbar to the parent's pack
                manager's packing list during initialization with `side="bottom"` and
                `fill="x"`.
        
                If you want to use the toolbar with a different layout manager,
                use `pack_toolbar=False`
        """
    def theme(self, theme: typing.Literal['light', 'dark']) -> None:
        """
        Change the color theme of the Toolbar.
        
                * `theme`: the theme name
        """
    @typing_extensions.override
    def destroy(self) -> None:
        ...

def set_mpl_default_theme(theme: typing.Literal['light', 'dark'], apply_font: bool) -> None:
    """
    Set default color constants of `matplotlib`.
    
        * `theme`: theme mode
        * `apply_font`: whether to use the font of `maliang`
    """
