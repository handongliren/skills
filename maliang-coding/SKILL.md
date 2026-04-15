---
name: maliang-coding
description: Guide AI agents to write correct maliang library code by providing function signatures and docstrings from pyi reference files. Use this skill whenever the user mentions maliang, tkinter UI, canvas-based UI, or asks to create/write/build UI components, widgets, animations, or themes using the maliang library. Trigger when user wants to use maliang for GUI development, asks about maliang APIs, or needs help writing maliang code.
---

# Maliang Coding Guide

This skill helps you write correct, syntactically accurate code for the **maliang** library - a lightweight UI framework based on `tkinter` with all UI drawn in Canvas.

## What is maliang?

maliang is a Python UI framework that provides:
- **Canvas-based rendering**: All widgets are drawn on Canvas, not native tkinter widgets
- **Theme support**: Built-in light/dark theme switching
- **Animations**: Rich animation system for smooth transitions
- **Modern widgets**: Button, Switch, InputBox, ProgressBar, Slider, etc.

**Key resources:**
- Website: https://xiaokang2022.github.io/maliang/
- GitHub: https://github.com/Xiaokang2022/maliang
- PyPI: https://pypi.org/project/maliang/

## How to Use This Skill

### Step 1: Identify What the User Needs

First, understand what kind of maliang code the user wants to write:
- **Container setup**: Tk, Toplevel, Canvas
- **Widgets**: Button, Label, InputBox, Switch, etc.
- **Animations**: MoveWidget, GradientItem, etc.
- **Colors/Themes**: Theme management, color utilities
- **Shapes/Images**: Drawing shapes, displaying images

### Step 2: Read the Relevant pyi Files

**CRITICAL**: Before writing ANY maliang code, you MUST read the appropriate `.pyi` file to get the exact function signatures and understand the parameters.

The pyi files are located in `references/pyi/` within this skill directory. Read them using the `read_file` tool:

| Category | File Path |
|----------|-----------|
| Main entry | `references/pyi/__init__.pyi` |
| Containers | `references/pyi/core/containers.pyi` |
| Base classes | `references/pyi/core/virtual.pyi` |
| Configs | `references/pyi/core/configs.pyi` |
| Widgets | `references/pyi/standard/widgets.pyi` |
| Shapes | `references/pyi/standard/shapes.pyi` |
| Texts | `references/pyi/standard/texts.pyi` |
| Images | `references/pyi/standard/images.pyi` |
| Dialogs | `references/pyi/standard/dialogs.pyi` |
| Animations | `references/pyi/animation/animations.pyi` |
| Controllers | `references/pyi/animation/controllers.pyi` |
| Color utils | `references/pyi/color/rgb.pyi`, `references/pyi/color/hsl.pyi`, `references/pyi/color/convert.pyi` |
| Theme manager | `references/pyi/theme/manager.pyi` |
| Enhanced tools | `references/pyi/toolbox/enhanced.pyi`, `references/pyi/toolbox/utility.pyi` |

### Step 3: Provide Accurate Code

After reading the pyi files, write code that:
1. **Matches exact signatures**: Use the correct parameter names and types
2. **Includes proper imports**: Import from the right modules
3. **Follows maliang patterns**: Use Canvas as parent, proper positioning, etc. **And remember that, you needn't use all patterns! Besides, when using Canvas, you must place it on master widget!**

### Step 4: Explain to the User

When providing code, also explain:
- What each function/class does (based on docstrings in pyi)
- Required vs optional parameters
- Common patterns and best practices

## Module Structure Overview

```
maliang/
├── core/           # Core containers and base classes
│   ├── containers.pyi  # Tk, Toplevel, Canvas
│   ├── virtual.pyi     # Widget, Element, Style, Feature base classes
│   └── configs.pyi     # Configuration utilities
│
├── standard/       # Standard widgets and elements
│   ├── widgets.pyi     # Button, Label, InputBox, Switch, etc.
│   ├── shapes.pyi      # Geometric shapes
│   ├── texts.pyi       # Text elements
│   ├── images.pyi      # Image elements
│   └── dialogs.pyi     # Dialog components
│
├── animation/      # Animation system
│   ├── animations.pyi  # Animation classes
│   └── controllers.pyi # Animation controllers
│
├── color/          # Color utilities
│   ├── rgb.pyi         # RGB functions
│   ├── hsl.pyi         # HSL functions
│   ├── convert.pyi     # Color conversion
│   └── colortable.pyi  # Color tables
│
├── theme/          # Theme management
│   └── manager.pyi     # Theme manager
│
└── toolbox/        # Enhanced utilities
    ├── enhanced.pyi    # Enhanced PhotoImage
    └── utility.pyi     # Utility functions
```

## Common Patterns

### Basic Application Structure

```python
import maliang

# Create main window
root = maliang.Tk(
    size=(800, 600),      # Window size
    position=None,        # Auto-position (or (x, y))
    title="My App",       # Window title
    icon=None             # Icon path or PhotoImage
)

# Create canvas (main container for widgets)
canvas = maliang.Canvas(
    master=root,
    expand="",            # '', 'x', 'y', or 'xy'
    auto_zoom=False,
    keep_ratio=None,
    free_anchor=False,
    auto_update=None,
    zoom_all_items=False
)

# Add widgets...
button = maliang.Button(
    master=canvas,
    position=(100, 100),
    size=(200, 50),
    text="Click Me",
    command=lambda: print("Clicked!")
)

# Run
root.mainloop()
```

### Key Concepts

1. **Containers hierarchy**: Tk/Toplevel → Canvas → Widget
2. **Positioning**: Widgets use `(x, y)` tuple for position relative to their master
3. **Sizing**: Widgets use `(width, height)` tuple or `None` for auto-size
4. **Theming**: Use `root.theme('light')` or `root.theme('dark')` to switch themes
5. **Animations**: Animation classes take duration (ms), controller function, and callback

## Widget Parameters Reference

Most widgets share common parameters. Here's a quick reference (verify exact signatures in pyi files):

| Parameter | Type | Description |
|-----------|------|-------------|
| `master` | Canvas/Widget | Parent container |
| `position` | tuple[int, int] | Position (x, y) |
| `size` | tuple[int, int] | None | Size (w, h) |
| `text` | str | Display text |
| `family` | str | None | Font family |
| `fontsize` | int | None | Font size |
| `weight` | 'normal' | 'bold' | Font weight |
| `command` | Callable | None | Callback function |
| `anchor` | 'center', 'nw', etc. | Anchor position |
| `image` | PhotoImage | None | Image to display |

## Writing Code Checklist

Before finalizing maliang code, verify:

- [ ] Read the relevant `.pyi` file for exact signatures
- [ ] Use correct import statements (`import maliang` or `from maliang import ...`)
- [ ] Create Tk first, then Canvas, then widgets
- [ ] Position parameters are tuples: `(x, y)` not `x, y`
- [ ] Size parameters are tuples: `(w, h)` or `None`
- [ ] String literals for font weight/slant match exactly: `'normal'`, `'bold'`, `'roman'`, `'italic'`
- [ ] Anchor values are one of: `'n'`, `'e'`, `'w'`, `'s'`, `'nw'`, `'ne'`, `'sw'`, `'se'`, `'center'`
- [ ] Literal type parameters match exactly (check pyi for valid values)

## Troubleshooting Tips

If code fails, check:
1. **Import errors**: Ensure maliang is installed (`pip install maliang`)
2. **Type errors**: Verify parameter types match pyi signatures
3. **Hierarchy errors**: Canvas must be created before widgets
4. **Position errors**: Positions are relative to master Canvas
5. **Theme errors**: Call `theme()` on Tk/Toplevel/Canvas, not on widgets

## Example Workflow

When user asks: "Create a maliang button that changes color on click"

1. Read `references/pyi/standard/widgets.pyi` to find Button class
2. Read `references/pyi/animation/animations.pyi` for color animation
3. Write code:

```python
import maliang
from maliang.animation import animations

root = maliang.Tk(size=(400, 300), position=None, title="Button Demo")
canvas = maliang.Canvas(master=root)

def on_click():
    print("Button clicked!")
    # Could add animation here

button = maliang.Button(
    master=canvas,
    position=(200, 150),
    size=(150, 40),
    text="Click Me",
    command=on_click
)

root.mainloop()
```

4. Explain: The Button widget is created on Canvas, positioned at (200, 150), with a click callback.

---

**Remember**: Always read the pyi files first to ensure syntactically correct code. The pyi files contain the authoritative function signatures and docstrings that describe each component's purpose and usage.

> Good luck!
