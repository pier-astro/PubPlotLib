Advanced Usage
===============

Professional Tick and Formatter Setup
-------------------------------------

PubPlotLib provides utilities for professional-looking axes.

Custom Tick Settings
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt
   import matplotlib.pyplot as plt

   fig, ax = pplt.subplots()

   # Apply custom tick settings
   pplt.set_ticks(
       ax,
       direction='in',    # 'in' or 'out'
       top=True,          # Show ticks on top
       right=True,        # Show ticks on right
       major_length=3.5,  # Major tick length in pt
       minor_length=1.75, # Minor tick length in pt
   )

Smart Axis Formatters
~~~~~~~~~~~~~~~~~~~~~

Fix scientific notation issues (e.g., "10^0" becoming "1"):

.. code-block:: python

   import pubplotlib as pplt
   import matplotlib.pyplot as plt
   import numpy as np

   fig, ax = pplt.subplots()

   # Log-log plot
   x = np.logspace(0, 3, 100)
   y = 10**(np.log10(x) * 0.5)
   ax.loglog(x, y)

   # Fix axis formatting
   pplt.set_formatter(ax)  # Applies to both axes

   # Or apply to specific axes
   pplt.set_formatter(ax, axis='x')
   pplt.set_formatter(ax, axis='y')

Batch Formatting
~~~~~~~~~~~~~~~~

Apply formatting to all axes in a figure at once:

.. code-block:: python

   import pubplotlib as pplt
   import matplotlib.pyplot as plt

   fig, axes = pplt.subplots(nrows=2, ncols=2)

   # Apply to all axes
   pplt.set_ticks()        # Uses current figure
   pplt.set_formatter()    # Uses current figure

   # Or apply to specific axes
   pplt.set_ticks(axes)
   pplt.set_formatter(axes)

Working with Multiple Figures
------------------------------

Switching Styles Between Figures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt

   # Set global style for first figure
   pplt.style.use('aanda')
   fig1, ax1 = pplt.subplots()
   ax1.plot([1, 2, 3], [1, 4, 9])

   # Create figure with different local style
   fig2, ax2 = pplt.subplots(style='apj')
   ax2.plot([1, 2, 3], [9, 4, 1])

   # First figure still uses 'aanda'
   # Global style is still 'aanda' (not changed)

Creating Subplots with Different Styles
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each call to ``subplots()`` or ``figure()`` can use its own style:

.. code-block:: python

   import pubplotlib as pplt

   # Global style
   pplt.style.use('aanda')

   # Figure 1: uses global style
   fig1, ax1 = pplt.subplots()

   # Figure 2: uses local style
   fig2, ax2 = pplt.subplots(style='presentation')

   # Figure 3: uses global style again
   fig3, ax3 = pplt.subplots()

Working with LaTeX
------------------

Enabling LaTeX Rendering
~~~~~~~~~~~~~~~~~~~~~~~~

For better typography when using LaTeX:

1. Edit your custom .mplstyle file and add:

.. code-block:: text

   text.usetex: True
   text.latex.preamble: \usepackage{amsmath}\usepackage{amssymb}

2. Register the custom style:

.. code-block:: python

   import pubplotlib as pplt

   my_style = pplt.Style(
       name='aanda_latex',
       onecol=3.54,
       twocol=7.25,
       mplstyle='aanda_latex.mplstyle'
   )
   my_style.register(overwrite=True)

3. Use it:

.. code-block:: python

   pplt.style.use('aanda_latex')
   fig, ax = pplt.subplots()

**Requirements**: You need a working LaTeX installation on your system.

Writing Math Expressions
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pplt
   import matplotlib.pyplot as plt

   pplt.style.use('aanda')
   fig, ax = pplt.subplots()

   x = [1, 2, 3, 4, 5]
   y = [i**2 for i in x]
   ax.plot(x, y)

   # Math expressions work with or without LaTeX
   ax.set_xlabel(r'$x$ (m)')
   ax.set_ylabel(r'$y = x^2$ (m$^2$)')
   ax.set_title(r'Quadratic Relationship')

   plt.show()

Saving Figures
--------------

Best Practices
~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt
   import matplotlib.pyplot as plt

   fig, ax = pplt.subplots(style='aanda')
   ax.plot([1, 2, 3], [1, 4, 9])

   # Save as PDF (recommended for papers)
   plt.savefig('figure.pdf', bbox_inches='tight', dpi=300)

   # Save as PNG (good for presentations)
   plt.savefig('figure.png', bbox_inches='tight', dpi=300)

Common Save Options
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   plt.savefig(
       'figure.pdf',
       bbox_inches='tight',  # Remove excess whitespace
       dpi=300,              # Resolution (300+ for print)
       transparent=False,    # Background color
       facecolor='white'     # Background color
   )

Accessing Style Registry
-------------------------

Get All Style Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt

   for style_name in pplt.style.available():
       s = pplt.style.get(style_name)
       print(f"{style_name}:")
       print(f"  One-column: {s.onecol}\"")
       print(f"  Two-column: {s.twocol}\"")
       if s.mplstyle:
           print(f"  Style file: {s.mplstyle}")

Directly Accessing Style Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import pubplotlib as pplt
   from pubplotlib.stylebuilder import user_style_dir, builtin_yaml_filename

   # User styles are stored in
   print(f"User styles: {user_style_dir}")

   # Built-in styles config is at
   print(f"Built-in config: {builtin_yaml_filename}")

Troubleshooting
---------------

Figures Look Different Than Expected
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Make sure the correct style is set: ``pplt.style.current()``
- Check that fonts are available: ``from pubplotlib.stylebuilder import check_fonts; check_fonts()``
- Verify matplotlib version: ``import matplotlib; print(matplotlib.__version__)``

Text Not Rendering Correctly
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- For LaTeX: ensure a LaTeX distribution is installed
- Clear Matplotlib font cache: ``rm -rf ~/.cache/matplotlib``
- Rebuild: ``python -c "import matplotlib.font_manager; matplotlib.font_manager._load_fontmanager(try_read_cache=False)"``

Inconsistent Figure Sizes
~~~~~~~~~~~~~~~~~~~~~~~~~~

- Don't override ``figsize`` in calls
- Don't add elements outside the (0,1) canvas bounds
- Use ``pplt.figure()`` or ``pplt.subplots()`` instead of ``plt.figure()``
