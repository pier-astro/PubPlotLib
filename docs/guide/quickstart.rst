Quick Start
===========

Basic Usage
-----------

Here's a minimal example to get you started:

.. code-block:: python

   import matplotlib.pyplot as plt
   import pubplotlib as pplt

   # Set your journal style
   pplt.style.use('aanda')

   # Create a figure with appropriate dimensions
   fig, ax = pplt.subplots()

   # Plot your data
   x = [1, 2, 3, 4, 5]
   y = [1, 4, 9, 16, 25]
   ax.plot(x, y, 'o-')

   ax.set_xlabel('X Label')
   ax.set_ylabel('Y Label')
   ax.set_title('My Publication-Ready Plot')

   # Apply professional formatting
   pplt.set_ticks(ax)
   pplt.set_formatter(ax)

   plt.show()

Available Styles
~~~~~~~~~~~~~~~~

Check what styles are available:

.. code-block:: python

   import pubplotlib as pplt
   print(pplt.style.available())

Output example:

.. code-block:: text

   ['aanda', 'apj', 'presentation']

Setting Styles Globally
~~~~~~~~~~~~~~~~~~~~~~~~

Set a style globally so all subsequent figures use it:

.. code-block:: python

   import pubplotlib as pplt
   import matplotlib.pyplot as plt

   # Set global style
   pplt.style.use('apj')

   # Now all figures will use the APJ style
   fig1, ax1 = pplt.subplots()
   fig2, ax2 = pplt.subplots()

Setting Styles Locally (Per-Figure)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply a style to a specific figure without changing the global style:

.. code-block:: python

   import pubplotlib as pplt
   import matplotlib.pyplot as plt

   # Set global style
   pplt.style.use('aanda')

   # Create a figure with a different style (doesn't affect global state)
   fig, ax = pplt.subplots(style='presentation')
   ax.plot([1, 2, 3], [1, 4, 9])

   # Next figure uses the global 'aanda' style
   fig2, ax2 = pplt.subplots()

Single vs. Double Column Figures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create double-column figures by setting ``twocols=True``:

.. code-block:: python

   import pubplotlib as pplt

   # Single-column (default)
   fig, ax = pplt.subplots(style='aanda')

   # Double-column
   fig, ax = pplt.subplots(style='aanda', twocols=True)

Controlling Figure Height
~~~~~~~~~~~~~~~~~~~~~~~~~~

Adjust figure height using the ``height_ratio`` parameter:

.. code-block:: python

   import pubplotlib as pplt

   # Default: height = width / golden_ratio
   fig, ax = pplt.subplots(style='aanda')

   # Custom: height = width * 0.5
   fig, ax = pplt.subplots(style='aanda', height_ratio=0.5)

   # Very tall figure: height = width * 2.0
   fig, ax = pplt.subplots(style='aanda', height_ratio=2.0)

Professional Tick and Formatter Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PubPlotLib provides utilities to make your axes look professional:

.. code-block:: python

   import matplotlib.pyplot as plt
   import pubplotlib as pplt
   import numpy as np

   fig, ax = pplt.subplots(style='aanda')

   x = np.logspace(0, 3, 100)
   y = 10**(np.log10(x) * 0.5)  # x^0.5
   ax.loglog(x, y)

   # Apply professional tick settings
   pplt.set_ticks(ax, direction='in', top=True, right=True)

   # Fix axis labels (no more "10^0" for 1)
   pplt.set_formatter(ax)

   ax.set_xlabel('X (log scale)')
   ax.set_ylabel('Y (log scale)')

   plt.show()

Getting Style Information
~~~~~~~~~~~~~~~~~~~~~~~~~~

Get details about a specific style:

.. code-block:: python

   import pubplotlib as pplt

   # Get the current active style
   current = pplt.style.current()
   print(f"Current style: {current}")

   # Get a specific style object
   s = pplt.style.get('aanda')
   print(f"One-column width: {s.onecol} inches")
   print(f"Two-column width: {s.twocol} inches")

Next Steps
~~~~~~~~~~

- Learn about `styling` and custom styles
- Explore `figure-sizing` options
- Check the `API reference` for detailed function documentation
- See `advanced` examples for complex use cases
