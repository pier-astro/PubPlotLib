try:
    from importlib.metadata import version
    __version__ = version("pubplotlib")
except Exception:
    __version__ = "0.3.0"  # fallback for development

from .pubplotlib import (
    golden, pt, cm,
    set_style, get_style,
    available_styles, restore,
    setup_figsize, figure, subplots,
    set_journal, style
)
from .formatter import set_formatter
from .ticksetter import set_ticks
from . import pubplotlib as _pubplotlib
from . import stylebuilder
from .stylebuilder import Style, Journal
from . import formatter

__all__ = [
    '__version__',
    'golden', 'pt', 'cm',
    'set_style', 'get_style',
    'available_styles', 'restore',
    'setup_figsize', 'figure', 'subplots',
    'set_journal', 'style',
    'set_formatter',
    'set_ticks',
    'Style', 'Journal',
]