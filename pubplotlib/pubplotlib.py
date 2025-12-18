import matplotlib.pyplot as plt  # type: ignore
import os
import yaml
from .stylebuilder import Style, Journal, assets_dir, builtin_yaml_filename, user_yaml_filename, user_style_dir

# --- Constants ---
golden = (1 + 5**0.5) / 2  # golden ratio
pt = 1 / 72.27             # points to inches
cm = 1 / 2.54              # centimeters to inches


# --- Defaults ---
_default_style = "aanda"
_current_style = None


# --- Registry ---
def _load_style_registry():
    # Load built-in styles
    builtin = {}
    if builtin_yaml_filename.exists():
        with open(builtin_yaml_filename, "r") as file:
            raw = yaml.safe_load(file) or {}
        for name, entry in raw.items():
            builtin[name] = Style(
                name=name,
                onecol=entry.get("onecol"),
                twocol=entry.get("twocol"),
                mplstyle=assets_dir.joinpath(entry.get("mplstyle")).as_posix() if entry.get("mplstyle") else None,
            )
    # Load user styles (override built-ins)
    user = {}
    if os.path.exists(user_yaml_filename):
        with open(user_yaml_filename, "r") as file:
            raw = yaml.safe_load(file) or {}
        for name, entry in raw.items():
            user[name] = Style(
                name=name,
                onecol=entry.get("onecol"),
                twocol=entry.get("twocol"),
                mplstyle=os.path.join(user_style_dir, entry.get("mplstyle")) if entry.get("mplstyle") else None,
            )
    # User styles override built-ins
    registry = {**builtin, **user}
    return registry

_style_registry = _load_style_registry()


def available_styles():
    """Return a list of available styles."""
    return list(_style_registry.keys())

def get_style(style=None):
    """Return a Style instance (from string or directly)."""
    if isinstance(style, Style):
        return style
    if style is not None:
        if style not in _style_registry:
            raise ValueError(f"Style '{style}' not found. Available: {available_styles()}")
        return _style_registry[style]
    # Use current style if set, otherwise fall back to default
    active_style = _current_style if _current_style is not None else _default_style
    return _style_registry[active_style]

def set_style(style=None):
    """Apply the style. Does nothing if already set."""
    global _current_style
    s = get_style(style)
    if _current_style == s.name:
        return
    if s.mplstyle is not None:
        plt.style.use(s.mplstyle)
    _current_style = s.name

def set_journal(journal=None):
    """Apply the journal style. Does nothing if already set."""
    return set_style(journal)


def restore():
    """Restore matplotlib's default style."""
    plt.style.use('default')


def _apply_style_local(style=None):
    """Apply a style locally without changing global state."""
    s = get_style(style)
    if s.mplstyle is not None:
        plt.style.use(s.mplstyle)
    return s


def setup_figsize(style=None, twocols=False, height_ratio=None):
    """Return (width, height) in inches for the style."""
    # If style is explicitly provided, apply it locally without changing global state
    # Otherwise, use the current global style
    if style is not None:
        s = _apply_style_local(style)
    else:
        s = _apply_style_local()  # Uses current global style
    
    width = s.twocol if twocols else s.onecol
    if width is None:
        raise ValueError(f"Style '{s.name}' does not support {'two' if twocols else 'one'}-column figures.")
    height = width / golden if height_ratio is None else width * height_ratio
    return width, height


def figure(style=None, twocols=False, height_ratio=None, journal=None, **kwargs):
    """Create a figure with style-appropriate dimensions."""
    width, height = setup_figsize(style or journal, twocols, height_ratio)
    return plt.figure(figsize=(width, height), **kwargs)

def subplots(style=None, twocols=False, height_ratio=None, journal=None, **kwargs):
    """Create subplots with style-appropriate dimensions."""
    width, height = setup_figsize(style or journal, twocols, height_ratio)
    return plt.subplots(figsize=(width, height), **kwargs)