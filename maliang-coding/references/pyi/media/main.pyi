"""APIs for playing videos"""

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
    """Provide the ability to switch icon theme."""


class _FullscreenToggleButton(widgets.ToggleButton, _CustomizedWidget):
    """Customized toggle button for function of fullscreen"""

    def __init__(self, *args, **kwargs) -> None: ...

class _AudioImage(widgets.Image, _CustomizedWidget):
    """Customized image widget for displaying audio icon"""

    def __init__(self, *args, **kwargs) -> None: ...

class _PlayButton(widgets.Button, _CustomizedWidget):
    """Customized Button for the ability to play or pause the video"""

    def __init__(self, *args, **kwargs) -> None: ...

class VideoCanvas(containers.Canvas):
    """A canvas that is scalable and playable for videos"""

    def __init__(self, master: containers.Tk | containers.Toplevel | containers.Canvas | None, controls: bool, loop: bool, click_pause: bool, expand: typing.Literal['', 'x', 'y', 'xy'], auto_zoom: bool, keep_ratio: typing.Literal['min', 'max'] | None, free_anchor: bool, **kwargs) -> None: ...
    @typing_extensions.override
    def zoom(self) -> None: ...
    def open(self, file: str, auto_play: bool, muted: bool) -> None: ...
    def close(self) -> None: ...
    @typing_extensions.override
    def destroy(self) -> None: ...
