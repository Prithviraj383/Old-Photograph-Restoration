"""
Tests for UI styling, theme switching, and component integrity.
Verifies the Vintage Studio UI styling, theme palettes, and icon ligature protection.
"""

import os
import sys
import unittest
import numpy as np

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from ui.styles import get_custom_css, LIGHT_PALETTE, DARK_PALETTE


class TestUIThemeAndStyles(unittest.TestCase):
    """Test suite for UI styling, CSS tokens, and theme handling."""

    def test_01_light_palette_values(self):
        """Verify Light Theme palette matches exact project specifications."""
        self.assertEqual(LIGHT_PALETTE["bg_primary"], "#F7F4EE")
        self.assertEqual(LIGHT_PALETTE["bg_secondary"], "#EFE9DF")
        self.assertEqual(LIGHT_PALETTE["text_primary"], "#302A24")
        self.assertEqual(LIGHT_PALETTE["text_secondary"], "#817568")
        self.assertEqual(LIGHT_PALETTE["accent"], "#806343")
        self.assertEqual(LIGHT_PALETTE["border"], "#E2D9CC")

    def test_02_dark_palette_values(self):
        """Verify Dark Theme palette matches exact project specifications."""
        self.assertEqual(DARK_PALETTE["bg_primary"], "#211F1D")
        self.assertEqual(DARK_PALETTE["bg_secondary"], "#2C2926")
        self.assertEqual(DARK_PALETTE["bg_card"], "#302C28")
        self.assertEqual(DARK_PALETTE["text_primary"], "#F3EBDD")
        self.assertEqual(DARK_PALETTE["text_secondary"], "#B5A89A")
        self.assertEqual(DARK_PALETTE["accent"], "#C29A6B")
        self.assertEqual(DARK_PALETTE["border"], "#494139")

    def test_03_no_broad_font_family_override(self):
        """Verify that [class*='st-'] font-family override was removed to prevent icon ligature breakage."""
        css_light = get_custom_css("light")
        css_dark = get_custom_css("dark")

        # Must not contain broad font-family override on [class*="st-"]
        self.assertNotIn('[class*="st-"]', css_light)
        self.assertNotIn('[class*="st-"]', css_dark)

        # Must protect Material Symbols icon fonts
        self.assertIn("Material Symbols Rounded", css_light)
        self.assertIn("Material Symbols Rounded", css_dark)

    def test_04_css_variable_generation(self):
        """Verify get_custom_css generates appropriate CSS variables for both themes."""
        css_light = get_custom_css("light")
        self.assertIn("--bg-primary: #F7F4EE", css_light)
        self.assertIn("--accent: #806343", css_light)

        css_dark = get_custom_css("dark")
        self.assertIn("--bg-primary: #211F1D", css_dark)
        self.assertIn("--accent: #C29A6B", css_dark)

    def test_05_button_contrast_colors(self):
        """Verify high contrast text colors on action buttons."""
        # Light mode: White text on deep bronze
        self.assertEqual(LIGHT_PALETTE["btn_primary_bg"], "#806343")
        self.assertEqual(LIGHT_PALETTE["btn_primary_text"], "#FFFFFF")

        # Dark mode: Solid dark text on warm golden amber (high contrast AAA)
        self.assertEqual(DARK_PALETTE["btn_primary_bg"], "#C29A6B")
        self.assertEqual(DARK_PALETTE["btn_primary_text"], "#1C1814")

    def test_06_navigation_link_overrides(self):
        """Verify CSS contains rules to override default blue link underlines."""
        css = get_custom_css("light")
        self.assertIn("text-decoration: none !important", css)
        self.assertIn(".studio-nav-link", css)


if __name__ == "__main__":
    unittest.main()
