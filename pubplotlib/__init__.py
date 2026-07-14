from ._version import __version__

# Auto-register bundled fonts with matplotlib so they work on all platforms
import os as _os
import matplotlib.font_manager as _fm
from importlib.resources import files as _files

_fonts_dir = _files("pubplotlib").joinpath("assets", "fonts")
if _fonts_dir.is_dir():
    for _font_file in sorted(_fonts_dir.iterdir()):
        _font_path = str(_font_file)
        if _font_path.lower().endswith(('.ttf', '.otf')):
            _fm.fontManager.addfont(_font_path)

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