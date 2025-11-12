from typing import Optional, Dict
import yaml
import os
import shutil
from importlib.resources import files
import matplotlib.font_manager as fm


# --- Module-level paths ---

# Built-in assets
assets_dir = files("pubplotlib").joinpath("assets")
builtin_yaml_filename = assets_dir.joinpath("styles.yaml")
core_styles = ['pubplot.mplstyle', 'aanda.mplstyle', 'apj.mplstyle']

# User config directory
user_dir = os.path.expanduser("~/.pubplotlib")
user_style_dir = os.path.join(user_dir, "style")
user_yaml_filename = os.path.join(user_dir, "styles.yaml")

# Ensure user directories exist
os.makedirs(user_style_dir, exist_ok=True)


def check_fonts(font_list=None, verbose=True):
    """
    Check if the required fonts are available to Matplotlib.
    Prints a summary and returns a dict {font_name: found_bool}.
    """
    if font_list is None:
        font_list = ["Times", "Arial", "Comic Sans"]  # Extend as needed
    available_fonts = set(f.name for f in fm.fontManager.ttflist)
    missing = [font for font in font_list if font not in available_fonts]
    found = {font: (font in available_fonts) for font in font_list}
    if verbose:
        if not missing:
            print("All the fonts are available.")
        else:
            print(
                f"{', '.join(missing)} fonts not available... "
                "If you intend to use them, install them and update the matplotlib cache:\n"
                "    python -c 'import matplotlib.font_manager; matplotlib.font_manager._get_fontconfig_fonts(); matplotlib.font_manager._load_fontmanager(try_read_cache=False)'"
            )
    return found


def build_builtin_styles(overwrite: bool = False) -> Dict[str, Dict[str, object]]:
    """
    Build and write the default built-in styles YAML file with standard styles (e.g., journals).
    Overwrites the file if overwrite=True.

    Args:
        overwrite: if True, overwrites the YAML file if it exists.

    Returns:
        The built-in style dict with dimensions in inches and style paths.
    """
    pt = 1 / 72.27  # points to inches conversion factor
    styles: Dict[str, Dict[str, object]] = {
        "aanda": {
            "onecol": 256.0 * pt,
            "twocol": 523.5 * pt,
            "mplstyle": "aanda.mplstyle",
        },
        "apj": {
            "onecol": 242.0 * pt,
            "mplstyle": "apj.mplstyle",
        },
    }

    if builtin_yaml_filename.exists() and not overwrite:
        raise FileExistsError(f"{builtin_yaml_filename} already exists. Use overwrite=True to overwrite.")

    with open(builtin_yaml_filename, "w", encoding="utf-8") as f:
        yaml.safe_dump(styles, f, default_flow_style=False)

    return styles


def remove_style(name: str):
    """
    Remove a user style from the user YAML registry and delete its style file.
    Built-in styles cannot be removed.

    Args:
        name: The name of the style to remove.
    """
    if not os.path.exists(user_yaml_filename):
        raise FileNotFoundError(f"{user_yaml_filename} does not exist.")

    with open(user_yaml_filename, "r", encoding="utf-8") as f:
        styles = yaml.safe_load(f) or {}

    if name not in styles:
        raise ValueError(f"Style '{name}' not found in {user_yaml_filename}.")

    style_filename = styles[name].get("mplstyle")
    style_path = os.path.join(user_style_dir, style_filename) if style_filename else None
    if style_filename and style_path and os.path.exists(style_path):
        os.remove(style_path)

    del styles[name]

    with open(user_yaml_filename, "w", encoding="utf-8") as f:
        yaml.safe_dump(styles, f, default_flow_style=False)



class Style:
    """
    Represents a generic figure formatting style (journal, slide, poster, etc).

    Attributes:
        name (str): The style's name.
        onecol (Optional[float]): Width of a single column (in inches).
        twocol (Optional[float]): Width of a double column (in inches).
        mplstyle (Optional[str]): Path to the associated .mplstyle file.
    """
    def __init__(
        self,
        name: str,
        onecol: Optional[float] = None,
        twocol: Optional[float] = None,
        mplstyle: Optional[str] = None,
    ):
        self.name = name
        self.onecol = onecol
        self.twocol = twocol
        self.mplstyle = mplstyle

        # Always store the style filename (not full path)
        if mplstyle is not None:
            if os.path.exists(mplstyle):
                style_filename = os.path.abspath(mplstyle)
            else:
                raise FileNotFoundError(f"Style file '{mplstyle}' does not exist.")
            self.mplstyle = style_filename

        if self.onecol is None and self.twocol is None:
            raise ValueError("At least one of 'onecol' or 'twocol' must be provided.")

    def register(self, overwrite: bool = False):
        """
        Register this Style in the user's styles YAML file.
        Copies the mplstyle file into the user's style directory if needed.

        Args:
            overwrite (bool): If True, overwrite existing entry and style file.
        """
        style_filename = os.path.basename(self.mplstyle) if self.mplstyle else None
        style_dest = os.path.join(user_style_dir, style_filename) if style_filename else None

        if style_filename:
            if os.path.exists(style_dest) and not overwrite:
                raise FileExistsError(f"Style file '{style_filename}' already exists in the user style directory. Use overwrite=True to replace it.")
            else:
                shutil.copyfile(self.mplstyle, style_dest)

        # Load or create the user YAML
        if os.path.exists(user_yaml_filename):
            with open(user_yaml_filename, "r", encoding="utf-8") as f:
                styles = yaml.safe_load(f) or {}
        else:
            styles = {}

        if self.name in styles and not overwrite:
            raise ValueError(
                f"Style '{self.name}' already exists in {user_yaml_filename}. Use overwrite=True to replace it or provide a different name."
            )

        styles[self.name] = {}
        if self.onecol is not None:
            styles[self.name]["onecol"] = self.onecol
        if self.twocol is not None:
            styles[self.name]["twocol"] = self.twocol
        styles[self.name]["mplstyle"] = style_filename  # Will be None if not provided

        with open(user_yaml_filename, "w", encoding="utf-8") as f:
            yaml.safe_dump(styles, f, default_flow_style=False)
        
    def __repr__(self):
        return (
            f"Style(name={self.name!r}, onecol={self.onecol}, "
            f"twocol={self.twocol}, mplstyle={self.mplstyle!r})"
        )

# Alias for backward compatibility
class Journal(Style):
    pass
