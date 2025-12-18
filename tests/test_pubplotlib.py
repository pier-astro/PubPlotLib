"""
Unit tests for PubPlotLib
"""

import unittest
import matplotlib.pyplot as plt
import pubplotlib as pplt


class TestStyleManager(unittest.TestCase):
    """Test the style manager functionality"""

    def setUp(self):
        """Set up test fixtures"""
        self.original_style = pplt.style.current()

    def tearDown(self):
        """Clean up after tests"""
        pplt.style.use(self.original_style)

    def test_available_styles(self):
        """Test that styles are available"""
        styles = pplt.style.available()
        self.assertIsInstance(styles, list)
        self.assertGreater(len(styles), 0)

    def test_style_use(self):
        """Test setting a style"""
        pplt.style.use('aanda')
        self.assertEqual(pplt.style.current(), 'aanda')

    def test_style_get(self):
        """Test getting a style object"""
        s = pplt.style.get('aanda')
        self.assertIsNotNone(s)
        self.assertIsNotNone(s.onecol)
        self.assertIsNotNone(s.twocol)

    def test_style_current(self):
        """Test getting current style"""
        pplt.style.use('aanda')
        current = pplt.style.current()
        self.assertEqual(current, 'aanda')


class TestFigureCreation(unittest.TestCase):
    """Test figure creation functions"""

    def tearDown(self):
        """Close all figures"""
        plt.close('all')

    def test_figure_creation(self):
        """Test creating a figure"""
        fig = pplt.figure(style='aanda')
        self.assertIsNotNone(fig)
        plt.close(fig)

    def test_subplots_creation(self):
        """Test creating subplots"""
        fig, ax = pplt.subplots(style='aanda')
        self.assertIsNotNone(fig)
        self.assertIsNotNone(ax)
        plt.close(fig)

    def test_figure_twocols(self):
        """Test creating a two-column figure"""
        fig, ax = pplt.subplots(style='aanda', twocols=True)
        self.assertIsNotNone(fig)
        plt.close(fig)

    def test_figure_height_ratio(self):
        """Test creating a figure with custom height ratio"""
        fig, ax = pplt.subplots(style='aanda', height_ratio=0.5)
        self.assertIsNotNone(fig)
        plt.close(fig)


class TestStyling(unittest.TestCase):
    """Test styling functionality"""

    def tearDown(self):
        """Clean up"""
        plt.close('all')

    def test_set_ticks(self):
        """Test setting ticks"""
        fig, ax = pplt.subplots()
        pplt.set_ticks(ax)
        self.assertIsNotNone(ax)
        plt.close(fig)

    def test_set_formatter(self):
        """Test setting formatter"""
        fig, ax = pplt.subplots()
        pplt.set_formatter(ax)
        self.assertIsNotNone(ax)
        plt.close(fig)


class TestSetupFigsize(unittest.TestCase):
    """Test figure sizing"""

    def test_setup_figsize_onecol(self):
        """Test single-column sizing"""
        width, height = pplt.setup_figsize(style='aanda', twocols=False)
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)

    def test_setup_figsize_twocol(self):
        """Test two-column sizing"""
        width, height = pplt.setup_figsize(style='aanda', twocols=True)
        self.assertGreater(width, 0)
        self.assertGreater(height, 0)

    def test_setup_figsize_custom_ratio(self):
        """Test custom height ratio"""
        width, height = pplt.setup_figsize(
            style='aanda',
            height_ratio=0.5
        )
        self.assertAlmostEqual(height, width * 0.5, places=2)


if __name__ == '__main__':
    unittest.main()
