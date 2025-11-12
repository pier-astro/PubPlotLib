# PubPlotLib

[![PyPI version](https://badge.fury.io/py/pubplotlib.svg)](https://badge.fury.io/py/pubplotlib)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

`PubPlotLib` is a Python library built on top of Matplotlib that simplifies the creation of publication-quality figures. It provides pre-configured styles and sizes for major scientific journals, allowing you to focus on your data, not the boilerplate code for plotting.

## Key Features

*   **Style-Ready Figures**: Automatically create figures with the correct dimensions and styles for journals, slides, posters, and more (A&A, ApJ, etc).
*   **Simple API**: Use `pubplotlib.figure` and `pubplotlib.subplots` as drop-in replacements for their Matplotlib counterparts.
*   **Flexible Sizing**: Easily switch between single-column and double-column layouts and control the aspect ratio.
*   **Smart Formatting**: Apply sensible defaults for axis tick formatters that avoid scientific notation for numbers like 1.0 (i.e., no more $10^0$).
*   **Customizable Ticks**: Fine-tune the appearance of major and minor ticks with a single function call.
*   **Extensible**: Add your own custom styles and sizes with ease.

## Installation

> **Note:** PubPlotLib requires Matplotlib version **3.2 or newer** for style support.

You can install PubPlotLib via pip:

```bash
pip install pubplotlib
```

## Quick Start

Creating a journal-styled figure is as simple as importing `pubplotlib` and using its `subplots` function.

```python
import numpy as np
import matplotlib.pyplot as plt
import pubplotlib as pplt

# 1. Set your target style (optional, can be done per-figure)
pplt.set_style('apj')

# 2. Create data
x = np.linspace(0.1, 10, 500)
y = np.sin(x) / x

# 3. Create a figure using pubplotlib's wrapper
fig, ax = pplt.subplots()
ax.plot(x, y)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Signal")

# 4. Customize ticks and formatters for a professional look
pplt.set_ticks(ax)
pplt.set_formatter(ax)

plt.show()
```

## Usage

### Figure Sizing

`PubPlotLib` makes it easy to create figures that fit perfectly into your manuscript's columns.

#### Single and Double Column Figures

Use the `twocols=True` argument to create a figure with the width of a double column.

```python
fig, ax = pplt.subplots(style='aanda', twocols=True)
ax.plot(...)
```

#### Custom Aspect Ratio

Control the figure's height using the `height_ratio` argument. The height will be `width * height_ratio`. If not provided, it defaults to the golden ratio.

```python
# Create a wide, short figure
fig, ax = pplt.subplots(twocols=True, height_ratio=0.3)
ax.plot(...)
```

#### Using Matplotlib's Default Figure and Subplots with Custom Sizing

We’ve hidden the `figsize` keyword in our API—because that’s the one thing that always messes up your image size when rendered in a paper!  
Instead, we set the figure width for you, and the `height_ratio` lets you decide how tall your image should be.

A couple of important notes:
1. **Don’t exceed the figure canvas!**  
   Adding extra axes or text outside the Matplotlib limits (beyond (1, 1)) will enlarge the image and ruin our careful setup for correct font sizes. If you need more axes, create a subgrid within your canvas and plot there.
2. **Using LaTeX?**  
   Don’t specify the width or height in `\includegraphics`! The figure is already sized perfectly. If you override this, you’ll corrupt the font sizes.  
   Use a plain approach like:
   ```latex
   \begin{figure}
     \centering
     \includegraphics{image.pdf}
     \caption{Hello World}
   \end{figure}
   ```

If you want to customize your plot, you can always use the default Matplotlib `figure` and `subplots` functions and specify the figure size yourself.  
To help, we provide the `onecol` and `twocol` attributes so you can shape your `figsize`:

```python
journal = pplt.get_style()
print("One column width:", journal.onecol)
print("Two column width:", journal.twocol)

fig, ax = plt.subplots(figsize=(journal.onecol, journal.onecol * 0.5))
ax.plot(...)
plt.show()
```

And for the truly bold:  
PubPlotLib exposes the Golden Ratio as `pplt.golden`, so you can size your figures like Leonardo da Vinci would have—just use `figsize=(journal.onecol, journal.onecol/pplt.golden)` (which, by the way, is our default)!


### Axis Styling: Better Ticks and Formatters

PubPlotLib makes it easy to create professional-looking axes with minimal effort:

- **Customizable Ticks:**  
  Use `pplt.set_ticks()` to control tick direction, length, and which sides show ticks.
  ```python
  fig, ax = pplt.subplots()
  ax.plot(...)
  # Show ticks on all sides, pointing inwards
  pplt.set_ticks(ax, direction='in', top=True, right=True)
  ```
  You can run `pplt.set_ticks()` without arguments to apply the default setup to all axes in the current figure.  
  If you want to apply it only to specific axes, pass the axis or a list of axes.  
  *Note:* For colorbars, a blind setup may affect the figure layout, so specify only the actual plot axes.

- **Smart Axis Formatters:**  
  Logarithmic axes in Matplotlib often format the number 1 as $10^0$.  
  Use `pplt.set_formatter()` to automatically format axis labels for clarity—numbers like `1` will show as `1`, not `$10^0$`.
  ```python
  fig, ax = pplt.subplots()
  ax.loglog(x, 10**(y*4))
  # Apply the formatter to both axes
  pplt.set_formatter(ax) # No more "10^0"!
  ```
  You can also run `pplt.set_formatter()` without arguments to apply the default formatter to all axes in the current figure.  
  For advanced use, PubPlotLib provides improved versions of Matplotlib's formatters:  
  - `pplt.formatter.ScalarFormatter`
  - `pplt.formatter.LogFormatterSciNotation`  
  Use these directly for custom formatting needs.

These functions help you avoid tedious manual axis formatting and ensure your figures look clean and publication-ready!



### Managing Styles

`PubPlotLib` comes with built-in support for several styles (journals, slides, posters, etc).

#### List Available Styles

See which styles are available out-of-the-box:

```python
print(pplt.available_styles())
```

#### Adding a New Style

You can easily define and register your own style.

1.  **Create a `Style` object**: Specify its name and column widths in inches. You can optionally link a `.mplstyle` file.

    ```python
    # Assumes 'my_style.mplstyle' exists in your working directory
    my_style = pplt.Style(
        name="my_style",
        onecol=3.5,          # 3.5 inches wide
        twocol=7.1,          # 7.1 inches wide
        mplstyle="my_style.mplstyle"
    )
    ```

2.  **Register the style**: This makes it available globally by copying the style file into your home directory and adding it to the configuration.

    ```python
    my_style.register(overwrite=True)
    ```

Now you can use it like any other style:

```python
fig, ax = pplt.subplots(style="my_style")
```

#### Removing a Style

You can remove a custom style you've added.

```python
pplt.stylebuilder.remove_style("my_style")
```

### Checking Fonts

Some styles require specific fonts (e.g., Times, ...). To check if these fonts are available to Matplotlib, run:

```python
from pubplotlib.stylebuilder import check_fonts
check_fonts()  # Prints a summary
```

If any fonts are missing, install them and update the Matplotlib font cache:

```bash
python -c "import matplotlib.font_manager; matplotlib.font_manager._get_fontconfig_fonts(); matplotlib.font_manager._load_fontmanager(try_read_cache=False)"
```
Or simply delete the cache and let Matplotlib rebuild it automatically:
```bash
rm -rf ~/.cache/matplotlib
```

We provide several fonts in the `fonts` folder of the repository—check there if you need them!

### LaTeX Font Rendering Engines

By default, PubPlotLib styles do **not** use LaTeX for font rendering, since requiring a LaTeX compiler can break the library for users who do not have one installed.

However, for some journals (e.g., A&A), LaTeX is used for typesetting, so matching font metrics and kerning is important (i.e. nicer).
To enable LaTeX rendering in Matplotlib, edit your `.mplstyle` file and add:

```
text.usetex: True
text.latex.preamble: \usepackage{amsmath}\usepackage{amssymb}  # For more math symbols
```

After editing, you can override the default journal style and save it locally.  
For example, to use your custom style with the same name as the default:

```python
import pubplotlib as pplt

# Register your custom style (assumes you have edited 'aanda.mplstyle')
my_style = pplt.Style(
    name="aanda",
    onecol=3.54,  # A&A one-column width in inches
    twocol=7.25,  # A&A two-column width in inches
    mplstyle="aanda.mplstyle"
)
my_style.register(overwrite=True)

# Now use your updated style
fig, ax = pplt.subplots(style="aanda")
ax.plot([1, 2, 3], [1, 4, 9])
plt.show()
```

**Note:**  
- You must have a working LaTeX installation for `text.usetex: True` to work.
- If you want to revert to the default style, remove your custom style using:
  ```python
  pplt.stylebuilder.remove_style("aanda")
  ```




## Contributing

Contributions are welcome! If you'd like to add a new style, fix a bug, or suggest an improvement, please open an issue or submit a pull request on our GitHub repository.