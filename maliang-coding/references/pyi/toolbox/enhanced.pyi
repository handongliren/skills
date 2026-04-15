"""
Enhanced versions of some ``tkinter`` classes and functions.
"""

from __future__ import annotations
import functools
import tkinter
from PIL import ImageTk

class PhotoImage(tkinter.PhotoImage):
    """
    Enhanced version of ``tkinter.PhotoImage``.
    """

    def scale(self, x: float, y: float) -> PhotoImage:
        """
        Scale the PhotoImage.
        
                    Args:
                        x: The x-axis scale factor.
                        y: The y-axis scale factor.
        
                    Returns:
                        A new scaled PhotoImage.
        """
    def resize(self, width: int, height: int) -> PhotoImage:
        """
        Resize the PhotoImage.
        
                    Args:
                        width: The new width of the image.
                        height: The new height of the image.
        
                    Returns:
                        A new resized PhotoImage.
        """

class PhotoImage(ImageTk.PhotoImage, tkinter.PhotoImage):
    """
    Pillow version of ``tkinter.PhotoImage``.
    """

    def scale(self, x: float, y: float) -> PhotoImage:
        """
        Scale the PhotoImage.
        
                    Args:
                        x: The x-axis scale factor.
                        y: The y-axis scale factor.
        
                    Returns:
                        A new scaled PhotoImage.
        """
    def resize(self, width: int, height: int) -> PhotoImage:
        """
        Resize the PhotoImage.
        
                    Args:
                        width: The new width of the image.
                        height: The new height of the image.
        
                    Returns:
                        A new resized PhotoImage.
        """
