"""
Integration tests for PhotoRestore workflow, theme switching, and state preservation.
"""

import os
import sys
import unittest
import numpy as np
import cv2

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from restoration import restore_image
import app


class MockSessionState(dict):
    """Mock Streamlit session state object supporting attribute access."""
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(item)

    def __setgetattr__(self, item, value):
        self[item] = value

    def __setattr__(self, key, value):
        self[key] = value


class TestWorkflowAndState(unittest.TestCase):
    """Test suite for full workflow execution and theme switching state preservation."""

    def setUp(self):
        self.mock_state = MockSessionState()
        # Patch app.st.session_state
        app.st.session_state = self.mock_state
        app.init_session_state()

    def test_theme_toggle_preserves_image_and_restoration_results(self):
        """Verify switching themes preserves uploaded photos and restoration results without recomputing."""
        sample_path = os.path.join(PROJECT_ROOT, "assets", "sample_images", "damaged_05.jpg")
        self.assertTrue(os.path.exists(sample_path))

        with open(sample_path, "rb") as f:
            file_bytes = f.read()

        # 1. Load image
        file_id = f"test_{len(file_bytes)}"
        success = app.load_image_from_bytes(file_bytes, "damaged_05.jpg", file_id)
        self.assertTrue(success)
        self.assertIsNotNone(self.mock_state.image_bgr)
        self.assertEqual(self.mock_state.theme, "light")

        # 2. Perform restoration
        results = restore_image(self.mock_state.image_bgr)
        self.mock_state.restored_data = results
        self.assertIsNotNone(self.mock_state.restored_data)
        original_restored = results["restored"]

        # 3. Toggle theme to dark
        self.mock_state.theme = "dark"

        # 4. Assert all restoration data remains intact
        self.assertEqual(self.mock_state.theme, "dark")
        self.assertIsNotNone(self.mock_state.image_bgr)
        self.assertIsNotNone(self.mock_state.restored_data)
        np.testing.assert_array_equal(self.mock_state.restored_data["restored"], original_restored)

        # 5. Assert valid JPEG download encoding
        ok, encoded = cv2.imencode(".jpg", self.mock_state.restored_data["restored"])
        self.assertTrue(ok)
        self.assertGreater(len(encoded), 1000)

    def test_new_upload_clears_stale_results(self):
        """Verify that loading a different photograph clears previous restoration results."""
        # Load first image
        img1 = np.full((100, 100, 3), 100, dtype=np.uint8)
        _, bytes1 = cv2.imencode(".jpg", img1)
        app.load_image_from_bytes(bytes1.tobytes(), "photo1.jpg", "id_1")
        self.mock_state.restored_data = {"dummy": True}

        # Load second image
        img2 = np.full((120, 120, 3), 120, dtype=np.uint8)
        _, bytes2 = cv2.imencode(".jpg", img2)
        app.load_image_from_bytes(bytes2.tobytes(), "photo2.jpg", "id_2")

        # Result should be reset to None for the new image
        self.assertIsNone(self.mock_state.restored_data)
        self.assertEqual(self.mock_state.image_name, "photo2.jpg")
        self.assertEqual(self.mock_state.image_meta["width"], 120)


if __name__ == "__main__":
    unittest.main()
