Styling Guide
==============

Understanding Styles
--------------------

A style in PubPlotLib consists of:

1. **Column Widths**: Figure dimensions for single and double-column layouts
2. **Matplotlib Style File (.mplstyle)**: Visual settings (fonts, colors, line widths, etc.)

Built-in Styles
~~~~~~~~~~~~~~~

PubPlotLib comes with several pre-configured styles:

- **aanda**: Astronomy & Astrophysics journal style
- **apj**: Astrophysical Journal style
- **presentation**: For presentations and slides

Applying Styles
---------------

Global Style
~~~~~~~~~~~~

Set a style globally so all subsequent figures use it:

.. code-block:: python

   import pubplotlib as pplt

   pplt.style.use('aanda')

   # All figures created after this will use 'aanda' style

Local Style (Per-Figure)
~~~~~~~~~~~~~~~~~~~~~~~~

Apply a style to a specific figure without affecting the global state:

.. code-block:: python

   import pubplotlib as pplt

   fig, ax = pplt.subplots(style='aanda')
   # This figure uses 'aanda' style
   # Global state is unchanged

   fig2, ax2 = pplt.subplots(style='apj')
   # This figure uses 'apj' style

Creating Custom Styles
----------------------

Create your own style by defining a new Style object:

.. code-block:: python

   import pubplotlib as pplt

   # Create a custom style
   my_style = pplt.Style(
       name='my_journal',
       onecol=3.5,        # Single-column width in inches
       twocol=7.0,        # Double-column width in inches
       mplstyle='my_style.mplstyle'  # Path to matplotlib style file
   )

Step 1: Create the .mplstyle File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file ``my_style.mplstyle`` with Matplotlib style settings:

.. code-block:: text

   # Font settings
   font.family: serif
   font.serif: Times, DejaVu Serif
   font.size: 10

   # Axes settings
   axes.labelsize: 10
   axes.titlesize: 12
   axes.linewidth: 0.8

   # Tick settings
   xtick.labelsize: 9
   ytick.labelsize: 9
   xtick.major.width: 0.8
   ytick.major.width: 0.8

   # Line and patch settings
   lines.linewidth: 1.5
   patch.linewidth: 0.8

   # Legend settings
   legend.fontsize: 9
   legend.framealpha: 0.9

   # Figure settings
   figure.autolayout: True
   savefig.format: pdf
   savefig.dpi: 300
   savefig.bbox: tight

Step 2: Register Your Style
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Register your style to make it available globally:

.. code-block:: python

   import pubplotlib as pplt

   my_style = pplt.Style(
       name='my_journal',
       onecol=3.5,
       twocol=7.0,
       mplstyle='my_style.mplstyle'
   )

   # Register the style (saves it to ~/.pubplotlib/style/)
   my_style.register(overwrite=True)

Now you can use it like a built-in style:

.. code-block:: python

   pplt.style.use('my_journal')
   fig, ax = pplt.subplots(style='my_journal')

Step 3 (Optional): Customize Further
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also create a custom .mplstyle by modifying an existing one:

.. code-block:: python

   import pubplotlib as pplt
   from pathlib import Path

   # Copy and modify the aanda style
   my_style = pplt.Style(
       name='aanda_custom',
       onecol=3.54,   # A&A standard
       twocol=7.25,   # A&A standard
       mplstyle='aanda_custom.mplstyle'
   )

   my_style.register(overwrite=True)

Managing Styles
---------------

View Available Styles
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt

   styles = pplt.style.available()
   for style_name in styles:
       s = pplt.style.get(style_name)
       print(f"{style_name}: {s.onecol}\" x ? (1 col), {s.twocol}\" x ? (2 col)")

Get Current Style
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt

   current = pplt.style.current()
   print(f"Current style: {current}")

Get Style Details
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt

   s = pplt.style.get('aanda')
   print(f"One-column: {s.onecol} inches")
   print(f"Two-column: {s.twocol} inches")
   print(f"Style file: {s.mplstyle}")

Remove a Custom Style
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt

   pplt.stylebuilder.remove_style('my_journal')

Matplotlib Style Files Reference
---------------------------------

Here are some common .mplstyle settings:

.. code-block:: text

   # Fonts
   font.family: serif | sans-serif | monospace
   font.size: 10
   font.serif: Times New Roman, Times, DejaVu Serif
   font.sans-serif: Arial, Helvetica, DejaVu Sans

   # Text rendering
   text.usetex: False | True  # Use LaTeX rendering
   text.latex.preamble: \usepackage{amsmath}

   # Axes
   axes.labelsize: 10
   axes.titlesize: 12
   axes.linewidth: 0.8
   axes.grid: False | True
   axes.axisbelow: True
   axes.xmargin: 0.0
   axes.ymargin: 0.05

   # Ticks
   xtick.labelsize: 9
   ytick.labelsize: 9
   xtick.major.size: 4
   xtick.minor.size: 2
   ytick.major.size: 4
   ytick.minor.size: 2
   xtick.major.width: 0.8
   xtick.minor.width: 0.6
   ytick.major.width: 0.8
   ytick.minor.width: 0.6
   xtick.direction: in | out
   ytick.direction: in | out

   # Lines and markers
   lines.linewidth: 1.5
   lines.markersize: 6

   # Legend
   legend.fontsize: 9
   legend.framealpha: 0.9
   legend.fancybox: True
   legend.loc: best

   # Figure
   figure.figsize: 8.0, 6.0  # width, height in inches
   figure.autolayout: True
   figure.titlesize: 14

   # Saving figures
   savefig.dpi: 300
   savefig.bbox: tight
   savefig.format: pdf
   savefig.transparent: False

For a complete reference, see `Matplotlib's style documentation <https://matplotlib.org/stable/tutorials/introductory/customizing.html>`_.
