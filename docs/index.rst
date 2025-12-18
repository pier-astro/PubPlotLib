PubPlotLib Documentation
========================

Welcome to **PubPlotLib**, a Python library for creating publication-quality figures with Matplotlib!

PubPlotLib simplifies the creation of figures that meet the specifications of major scientific journals, allowing you to focus on your data rather than formatting details.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   guide/installation
   guide/quickstart
   guide/styling
   guide/figure-sizing
   guide/advanced
   api/reference

Features
--------

✨ **Key Highlights**:

- **Journal-Ready Styles**: Pre-configured styles for A&A, ApJ, and custom journals
- **Smart Figure Sizing**: Automatic width and height calculation for single and double-column layouts
- **Professional Formatting**: Built-in tick and formatter utilities for polished axes
- **Easy Customization**: Create and register your own styles
- **Matplotlib Compatible**: Works seamlessly with Matplotlib's API

Quick Example
-------------

.. code-block:: python

   import matplotlib.pyplot as plt
   import pubplotlib as pplt

   # Set your journal style
   pplt.style.use('aanda')

   # Create a publication-ready figure
   fig, ax = pplt.subplots()
   ax.plot([1, 2, 3], [1, 4, 9])
   ax.set_xlabel('X-axis')
   ax.set_ylabel('Y-axis')

   # Apply professional formatting
   pplt.set_ticks(ax)
   pplt.set_formatter(ax)

   plt.savefig('figure.pdf')

Installation
------------

Install via pip:

.. code-block:: bash

   pip install pubplotlib

Or from GitHub:

.. code-block:: bash

   git clone https://github.com/pier-astro/PubPlotLib.git
   cd PubPlotLib
   pip install .

Requirements
~~~~~~~~~~~~

- Python ≥ 3.8
- Matplotlib ≥ 3.4
- PyYAML ≥ 5.3

Getting Help
~~~~~~~~~~~~

- 📖 Check the `guide` section for tutorials
- 🔧 See the `API reference` for detailed documentation
- 🐛 Report issues on `GitHub <https://github.com/pier-astro/PubPlotLib/issues>`_
- 💬 Discuss on `GitHub Discussions <https://github.com/pier-astro/PubPlotLib/discussions>`_

Contributing
~~~~~~~~~~~~

Contributions are welcome! Please visit our `GitHub repository <https://github.com/pier-astro/PubPlotLib>`_.

License
-------

PubPlotLib is licensed under the GNU General Public License v3.0. See `LICENSE <https://github.com/pier-astro/PubPlotLib/blob/main/LICENSE>`_ for details.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
