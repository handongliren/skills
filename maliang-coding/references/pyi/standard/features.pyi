"""All standard ``Feature`` classes."""

from __future__ import annotations
from typing import TYPE_CHECKING
from typing_extensions import override
from ..animation import animations, controllers
from ..core import virtual
from ..standard import shapes
from ..toolbox import utility
import tkinter
from collections.abc import Callable
from typing import Any

class TextFeature(virtual.Feature):
    """Feature of Text."""


class ImageFeature(virtual.Feature):
    """Feature of Image."""


class LabelFeature(virtual.Feature):
    """Feature of Label."""


class ButtonFeature(virtual.Feature):
    """Feature of Button."""

    def __init__(self, widget: virtual.Widget, command: Callable | None, args: tuple) -> None: ...

class Underline(ButtonFeature):
    """Feature of underline."""


class Highlight(ButtonFeature):
    """Feature of highlight."""


class SwitchFeature(ButtonFeature):
    """Feature of Switch."""


class ToggleButtonFeature(ButtonFeature):
    """Feature of ToggleButton."""


class CheckBoxFeature(ToggleButtonFeature):
    """Feature of CheckButton."""


class RadioBoxFeature(ButtonFeature):
    """Feature of RadioButton."""


class ProgressBarFeature(LabelFeature):
    """Feature of ProgressBar."""


class InputBoxFeature(ButtonFeature):
    """Feature of input box."""

    def __init__(self, widget: virtual.Widget, command: Callable[..., Any] | None, args: tuple) -> None: ...

class SliderFeature(virtual.Feature):
    """Feature of Slider."""

    def __init__(self, widget: virtual.Widget) -> None: ...

class SegmentedButtonFeature(virtual.Feature):
    """Feature of SegmentedButton."""


class SpinBoxFeature(virtual.Feature):
    """Feature of SpinBox."""

    def __init__(self, widget: virtual.Widget, command: Callable[[bool], Any] | None) -> None: ...
