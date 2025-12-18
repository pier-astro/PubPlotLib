API Reference
=============

Main Functions
--------------

Figure and Subplot Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autofunction:: pubplotlib.figure
   :noindex:

.. autofunction:: pubplotlib.subplots
   :noindex:

Style Management
~~~~~~~~~~~~~~~~

.. autofunction:: pubplotlib.set_style
   :noindex:

.. autofunction:: pubplotlib.set_journal
   :noindex:

.. autofunction:: pubplotlib.get_style
   :noindex:

.. autofunction:: pubplotlib.available_styles
   :noindex:

.. autofunction:: pubplotlib.restore
   :noindex:

Figure Sizing
~~~~~~~~~~~~~

.. autofunction:: pubplotlib.setup_figsize
   :noindex:

Axis Formatting
~~~~~~~~~~~~~~~

.. autofunction:: pubplotlib.set_ticks
   :noindex:

.. autofunction:: pubplotlib.set_formatter
   :noindex:

Style Namespace
---------------

The ``pplt.style`` object provides a matplotlib-like interface:

.. autoclass:: pubplotlib.pubplotlib._StyleManager
   :members:
   :undoc-members:

Style Objects
~~~~~~~~~~~~~

.. autoclass:: pubplotlib.stylebuilder.Style
   :members:
   :undoc-members:

.. autoclass:: pubplotlib.stylebuilder.Journal
   :members:
   :undoc-members:

Constants
---------

.. autodata:: pubplotlib.golden
   :noindex:

.. autodata:: pubplotlib.pt
   :noindex:

.. autodata:: pubplotlib.cm
   :noindex:

Formatter Utilities
-------------------

.. autoclass:: pubplotlib.formatter.ScalarFormatter
   :members:
   :undoc-members:

.. autoclass:: pubplotlib.formatter.LogFormatterSciNotation
   :members:
   :undoc-members:

Style Builder Module
---------------------

.. automodule:: pubplotlib.stylebuilder
   :members:
   :undoc-members:
   :show-inheritance:

Formatter Module
----------------

.. automodule:: pubplotlib.formatter
   :members:
   :undoc-members:
   :show-inheritance:

Tick Setter Module
------------------

.. automodule:: pubplotlib.ticksetter
   :members:
   :undoc-members:
   :show-inheritance:

Complete Module Reference
--------------------------

.. automodule:: pubplotlib
   :members:
   :undoc-members:
   :show-inheritance:
