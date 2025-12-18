Figure Sizing
==============

One of PubPlotLib's key features is automatic figure sizing for publication-ready dimensions.

Basic Sizing
~~~~~~~~~~~~

By default, figures are sized according to the selected style:

.. code-block:: python

   import pubplotlib as pplt

   # Single-column figure (default)
   fig, ax = pplt.subplots(style='aanda')

   # Double-column figure
   fig, ax = pplt.subplots(style='aanda', twocols=True)

The width is set automatically, and the height is calculated using the golden ratio.

Custom Height
~~~~~~~~~~~~~

Control the height using the ``height_ratio`` parameter:

.. code-block:: python

   import pubplotlib as pplt

   # height = width * height_ratio
   fig, ax = pplt.subplots(
       style='aanda',
       height_ratio=0.5  # Wider, shorter figure
   )

Examples of common aspect ratios:

- ``height_ratio=0.5``: Wide, short figure (good for time series)
- ``height_ratio=1.0``: Nearly square
- ``height_ratio=pplt.golden`` or None (default): Golden ratio
- ``height_ratio=1.5``: Tall, narrow figure (good for profiles)
- ``height_ratio=2.0``: Very tall figure

Accessing Style Dimensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can access the column widths directly:

.. code-block:: python

   import pubplotlib as pplt

   s = pplt.style.get('aanda')
   print(f"One-column width: {s.onecol} inches")
   print(f"Two-column width: {s.twocol} inches")

Or get the current style's dimensions:

.. code-block:: python

   import pubplotlib as pplt

   pplt.style.use('aanda')
   s = pplt.style.get()  # Gets current style
   print(s.onecol, s.twocol)

Using with Standard Matplotlib
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use standard Matplotlib but need the correct dimensions:

.. code-block:: python

   import matplotlib.pyplot as plt
   import pubplotlib as pplt

   s = pplt.style.get('aanda')
   width = s.onecol
   height = width / pplt.golden  # or width * height_ratio

   fig, ax = plt.subplots(figsize=(width, height))
   ax.plot([1, 2, 3], [1, 4, 9])

Important Notes
~~~~~~~~~~~~~~~

**Don't Override Dimensions in LaTeX**

When using figures in LaTeX, do NOT specify width in ``\includegraphics``:

.. code-block:: latex

   % WRONG - corrupts font sizes
   \includegraphics[width=\textwidth]{figure.pdf}

   % CORRECT - use default dimensions
   \includegraphics{figure.pdf}

**Don't Exceed Canvas Bounds**

Keep all plot elements within the figure canvas. Adding elements outside the (0,1) range will enlarge the figure and break the sizing.

**Golden Ratio**

PubPlotLib uses the golden ratio (φ ≈ 1.618) as the default height ratio:

.. code-block:: python

   import pubplotlib as pplt

   print(pplt.golden)  # ~1.618
   # Default height = width / pplt.golden

You can use it explicitly:

.. code-block:: python

   fig, ax = pplt.subplots(height_ratio=1/pplt.golden)

Subplots with Custom Sizing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For subplots, the overall figure size follows the styling rules:

.. code-block:: python

   import pubplotlib as pplt

   fig, (ax1, ax2) = pplt.subplots(
       style='aanda',
       nrows=2,
       ncols=1,
       height_ratio=1.5  # Tall figure for two stacked plots
   )

   ax1.plot([1, 2, 3], [1, 4, 9])
   ax2.plot([1, 2, 3], [9, 4, 1])
