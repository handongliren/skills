"""
All standard ``Style`` classes.
"""

from __future__ import annotations
import copy
from typing import TYPE_CHECKING
from typing_extensions import override
from ..core import virtual
import types
from typing import Literal

class TextStyle(virtual.Style):
    """
    Style of Text.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``
        
                Args:
                    theme: The theme to apply the style to.
                    fg: The foreground color of the widget.
        """

class LabelStyle(virtual.Style):
    """
    Style of Label.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``
        
                Args:
                    theme: The theme to apply the style to.
                    fg: The foreground color of the widget.
                    bg: The background color of the widget.
                    ol: The outline color of the widget.
        """

class ButtonStyle(LabelStyle):
    """
    Style of Button.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``, ``"active"``
        
                Args:
                    theme: the theme name, None indicates both.
                    fg: the foreground color of the widget.
                    bg: the background color of the widget.
                    ol: the outline color of the widget.
        """

class SwitchStyle(virtual.Style):
    """
    Style of Switch.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg_slot: tuple[str | types.EllipsisType, ...] | str | None, ol_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_dot: tuple[str | types.EllipsisType, ...] | str | None, ol_dot: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal-off"``, ``"hover-off"``, ``"active-off"``,
                ``"normal-on"``, ``"hover-on"``, ``"active-on"``
        
                Args:
                    theme: the theme name, None indicates both.
                    bg_slot: the background color of the widget.
                    ol_slot: the outline color of the widget.
                    bg_dot: the inside background color of the widget.
                    ol_dot: the inside outline color of the widget.
        """

class InputBoxStyle(virtual.Style):
    """
    Style of InputBox.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None, bg_bar: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``, ``"active"``
        
                Args:
                    theme: the theme name, None indicates both.
                    fg: the foreground color of the widget.
                    bg: the background color of the widget.
                    ol: the outline color of the widget.
                    bg_bar: the highlight bar of the widget (Only for Windows11 theme).
        """

class ToggleButtonStyle(virtual.Style):
    """
    Style of ToggleButton.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal-off"``, ``"hover-off"``, ``"active-off"``,
                ``"normal-on"``, ``"hover-on"``, ``"active-on"``
        
                Args:
                    theme: the theme name, None indicates both.
                    fg: the foreground color of the widget.
                    bg: the background color of the widget.
                    ol: the outline color of the widget.
        """

class CheckBoxStyle(ToggleButtonStyle):
    """
    Style of CheckBox.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    states: tuple[str, ...]
    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class RadioBoxStyle(virtual.Style):
    """
    Style of RadioGroup.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg_box: tuple[str | types.EllipsisType, ...] | str | None, ol_box: tuple[str | types.EllipsisType, ...] | str | None, bg_dot: tuple[str | types.EllipsisType, ...] | str | None, ol_dot: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``, ``"active"``
        
                Args:
                    theme: the theme name, None indicates both.
                    bg_box: the background color of the widget.
                    ol_box: the outline color of the widget.
                    bg_dot: the inside background color of the widget.
                    ol_dot: the inside outline color of the widget.
        """

class ProgressBarStyle(virtual.Style):
    """
    Style of ProgressBar.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg_slot: tuple[str | types.EllipsisType, ...] | str | None, ol_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_bar: tuple[str | types.EllipsisType, ...] | str | None, ol_bar: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``
        
                Args:
                    theme: the theme name, None indicates both.
                    bg_slot: the background color of the widget.
                    ol_slot: the outline color of the widget.
                    bg_bar: the inside background color of the widget.
                    ol_bar: the inside outline color of the widget.
        """

class UnderlineButtonStyle(TextStyle):
    """
    Style of UnderlineButton.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class HighlightButtonStyle(TextStyle):
    """
    Style of HighlightButtonStyle.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class IconButtonStyle(LabelStyle):
    """
    Style of IconButtonStyle.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]

class SliderStyle(virtual.Style):
    """
    Style of Slider.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_slot: tuple[str | types.EllipsisType, ...] | str | None, bg_pnt: tuple[str | types.EllipsisType, ...] | str | None, bg_dot: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``, ``"active"``
        
                Args:
                    theme: the theme name, None indicates both.
                    fg_slot: the foreground color of the widget.
                    bg_slot: the background color of the widget.
                    bg_pnt: the pointer color of the widget.
                    bg_dot: the pointer highlight part color of the widget (Only for
                        Windows11 theme).
        """

class SegmentedButtonStyle(virtual.Style):
    """
    Style of SegmentedButton.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``
        
                Args:
                    theme: the theme name, None indicates both.
                    bg: the background color of the widget.
                    ol: the outline color of the widget.
        """

class ToggleButtonStyle4SB(ToggleButtonStyle):
    """
    style of ToggelButton for SegmentedButton.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light = copy.deepcopy(ToggleButtonStyle.light)
    dark = copy.deepcopy(ToggleButtonStyle.dark)

class OptionButtonStyle(virtual.Style):
    """
    Style of OptionButton.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``, ``"hover"``, ``"active"``
        
                Args:
                    theme: the theme name, None indicates both.
                    bg: the background color of the widget.
                    ol: the outline color of the widget.
        """

class SpinnerStyle(virtual.Style):
    """
    Style of Spinner.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``
        
                Args:
                    theme: the theme name, None indicates both.
                    fg: the foreground color of the widget.
                    bg: the background color of the widget.
        """

class TooltipStyle(virtual.Style):
    """
    Style of Tooltip.
    
        Attributes:
            states (tuple[str, ...]): all states of the widget.
            light (dict[str, dict[str, dict[str, str]]]):
                The light theme style dictionary.
            dark (dict[str, dict[str, dict[str, str]]]):
                The dark theme style dictionary.
    """

    light: dict[str, dict[str, dict[str, str]]]
    dark: dict[str, dict[str, dict[str, str]]]
    @override
    def set(self, theme: Literal['light', 'dark'] | None, fg: tuple[str | types.EllipsisType, ...] | str | None, bg: tuple[str | types.EllipsisType, ...] | str | None, ol: tuple[str | types.EllipsisType, ...] | str | None) -> None:
        """
        Set the style of the widget.
        
                states: ``"normal"``
        
                Args:
                    theme: the theme name, None indicates both.
                    fg: the foreground color of the widget.
                    bg: the background color of the widget.
                    ol: the outline color of the widget.
        """
