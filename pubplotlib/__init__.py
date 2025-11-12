from .pubplotlib import (
    golden, pt, cm,
    set_style, get_style,
    available_styles, restore,
    setup_figsize, figure, subplots,
    set_journal
)
from .formatter import set_formatter
from .ticksetter import set_ticks
from . import pubplotlib as _pubplotlib
from . import stylebuilder
from .stylebuilder import Style, Journal
from . import formatter