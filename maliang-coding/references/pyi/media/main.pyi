"""
APIs for playing videos
"""

from __future__ import annotations
import abc
import platform
import time
import typing
import ffpyplayer.pic
import ffpyplayer.player
import PIL.Image
import PIL.ImageTk
import typing_extensions
from maliang.animation import animations, controllers
from maliang.core import containers, virtual
from maliang.standard import images, widgets
from maliang.theme import manager
from maliang.toolbox import enhanced
from . import icons

class _CustomizedWidget(virtual.Widget, abc.ABC):
    """
    Provide the ability to switch icon theme.
    """


class _FullscreenToggleButton(widgets.ToggleButton, _CustomizedWidget):
    """
    Customized toggle button for function of fullscreen
    """

    def __init__(self, *args, **kwargs) -> None:
        ...

class _AudioImage(widgets.Image, _CustomizedWidget):
    """
    Customized image widget for displaying audio icon
    """

    def __init__(self, *args, **kwargs) -> None:
        ...

class _PlayButton(widgets.Button, _CustomizedWidget):
    """
    Customized Button for the ability to play or pause the video
    """

    def __init__(self, *args, **kwargs) -> None:
        ...

class VideoCanvas(containers.Canvas):
    """
    A canvas that is scalable and playable for videos
    """

    def __init__(self, master: containers.Tk | containers.Toplevel | containers.Canvas | None, controls: bool, loop: bool, click_pause: bool, expand: typing.Literal['', 'x', 'y', 'xy'], auto_zoom: bool, keep_ratio: typing.Literal['min', 'max'] | None, free_anchor: bool, **kwargs) -> None:
        """
        * `master`: parent widget
                * `controls`: whether to enable the built-in UI
                * `loop`: whether the video loops automatically
                * `click_pause`: whether to pause when clicked
                * `expand`: the mode of expand, `x` is horizontal, and `y` is vertical
                * `auto_zoom`: whether or not to scale its items
                * `keep_ratio`: the mode of aspect ratio, `min` follows the minimum
                value, `max` follows the maximum value
                * `free_anchor`: whether the anchor point is free-floating
                * `kwargs`: compatible with other parameters of class `tkinter.Canvas`
        """
    @typing_extensions.override
    def zoom(self) -> None:
        ...
    def open(self, file: str, auto_play: bool, muted: bool) -> None:
        """
        Open a video file and play
        
                * `file`: the video file path
                * `auto_play`: whether to start playing the video automatically
                * `muted`: whether or not to mute the video at the start
        """
    def close(self) -> None:
        """
        Close the video player
        """
    @typing_extensions.override
    def destroy(self) -> None:
        ...
