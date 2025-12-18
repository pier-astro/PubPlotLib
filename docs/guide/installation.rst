Installation
=============

Requirements
~~~~~~~~~~~~

- Python ≥ 3.8
- Matplotlib ≥ 3.4
- PyYAML ≥ 5.3

From PyPI
---------

The easiest way to install PubPlotLib is via pip:

.. code-block:: bash

   pip install pubplotlib

From GitHub
-----------

To install the latest development version directly from GitHub:

.. code-block:: bash

   git clone https://github.com/pier-astro/PubPlotLib.git
   cd PubPlotLib
   pip install .

For development, install with dev dependencies:

.. code-block:: bash

   pip install -e ".[dev]"

Verifying Installation
~~~~~~~~~~~~~~~~~~~~~~

To verify your installation, run:

.. code-block:: python

   import pubplotlib as pplt
   print(pplt.available_styles())

You should see a list of available styles like ``['aanda', 'apj', 'presentation']``.

Font Requirements
~~~~~~~~~~~~~~~~~

Some styles may require specific fonts (e.g., Times New Roman). To check if all required fonts are available:

.. code-block:: python

   from pubplotlib.stylebuilder import check_fonts
   check_fonts()

If fonts are missing, you can:

1. Install them system-wide (varies by OS)
2. Use the fonts provided in the ``fonts/`` folder of the repository
3. Update Matplotlib's font cache:

.. code-block:: bash

   python -c "import matplotlib.font_manager; matplotlib.font_manager._load_fontmanager(try_read_cache=False)"

Or clear the cache and let Matplotlib rebuild it:

.. code-block:: bash

   rm -rf ~/.cache/matplotlib

Troubleshooting
~~~~~~~~~~~~~~~

**ImportError: No module named 'pubplotlib'**

Make sure you're in the correct Python environment and that the package was installed:

.. code-block:: bash

   pip list | grep pubplotlib

**Matplotlib version too old**

Update Matplotlib to version 3.4 or newer:

.. code-block:: bash

   pip install --upgrade matplotlib

**Font not found errors**

See the "Font Requirements" section above.
