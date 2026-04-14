"""All standard ``Style`` classes."""

from __future__ import annotations
import copy
import types
from typing import Literal
from typing_extensions import override
from ..core import virtual

class TextStyle(virtual.Style):
    """Style of Text.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class LabelStyle(virtual.Style):
    """Style of Label.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class ButtonStyle(LabelStyle):
    """Style of Button.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class SwitchStyle(virtual.Style):
    """Style of Switch.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg_slot: tuple[str | types.EllipsisType, ...] | str | None, ol_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_dot: tuple[str | types.EllipsisType, ...] | str | None, ol_dot: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class InputBoxStyle(virtual.Style):
    """Style of InputBox.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None, bg_bar: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class ToggleButtonStyle(virtual.Style):
    """Style of ToggleButton.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class CheckBoxStyle(ToggleButtonStyle):
    """Style of CheckBox.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class RadioBoxStyle(virtual.Style):
    """Style of RadioGroup.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg_box: tuple[str | types.EllipsisType, ...] | str | None, ol_box: tuple[str | types.EllipsisType, ...] | str | None, bg_dot: tuple[str | types.EllipsisType, ...] | str | None, ol_dot: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class ProgressBarStyle(virtual.Style):
    """Style of ProgressBar.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg_slot: tuple[str | types.EllipsisType, ...] | str | None, ol_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_bar: tuple[str | types.EllipsisType, ...] | str | None, ol_bar: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class UnderlineButtonStyle(TextStyle):
    """Style of UnderlineButton.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class HighlightButtonStyle(TextStyle):
    """Style of HighlightButtonStyle.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class IconButtonStyle(LabelStyle):
    """Style of IconButtonStyle.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class SliderStyle(virtual.Style):
    """Style of Slider.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_pnt: tuple[str | types.EllipsisType, ...] | str | None, bg_dot: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class SegmentedButtonStyle(virtual.Style):
    """Style of SegmentedButton.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class ToggleButtonStyle4SB(ToggleButtonStyle):
    """style of ToggelButton for SegmentedButton.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light = copy.deepcopy(ToggleButtonStyle.light)
    dark = copy.deepcopy(ToggleButtonStyle.dark)

class OptionButtonStyle(virtual.Style):
    """Style of OptionButton.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class SpinnerStyle(virtual.Style):
    """Style of Spinner.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...

class TooltipStyle(virtual.Style):
    """Style of Tooltip.

    Attributes:
        states (tuple[str, ...]): all states of the widget.
        light (dict[str, dict[str, dict[str, str]]]):
            The light theme style dictionary.
        dark (dict[str, dict[str, dict[str, str]]]):
            The dark theme style dictionary."""

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None: ...
