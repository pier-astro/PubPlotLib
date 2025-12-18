# Changelog

All notable changes to PubPlotLib will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-12-18

### Added
- New `pplt.style` namespace with matplotlib-like API
  - `pplt.style.use()` - Set global style
  - `pplt.style.available()` - List available styles
  - `pplt.style.get()` - Get style object
  - `pplt.style.current()` - Get current style
  - `pplt.style.restore()` - Restore defaults
- Local style application - styles passed to `figure()` or `subplots()` no longer change global state
- Comprehensive documentation via Sphinx + ReadTheDocs
- Unit tests with pytest
- PyPI package metadata and publishing support

### Changed
- Updated documentation to use new `pplt.style.use()` API
- Improved figure sizing with better height ratio handling

### Deprecated
- `pplt.set_style()` is still available but `pplt.style.use()` is recommended for new code

## [0.1.0] - 2024-01-01

### Added
- Initial release
- Built-in styles: `aanda`, `apj`, `presentation`
- Figure sizing for single and double-column layouts
- Tick and formatter utilities
- Style registration system for custom styles
- Basic documentation and examples
