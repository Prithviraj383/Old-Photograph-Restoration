"""
Tests for PhotoRestore - Old Photograph Restoration.
Verifies the existing restoration function's behavior without modifying restoration.py.
"""

import os
import sys
import unittest
import numpy as np
import cv2

# Ensure project root is in sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


class TestRestoration(unittest.TestCase):
    """Test suite for the restore_image function in restoration.py."""

    def test_01_import_restoration(self):
        """1. Verify the restoration function can be imported."""
        try:
            from restoration import restore_image
            self.assertTrue(callable(restore_image))
        except ImportError as e:
            self.fail(f"Failed to import restore_image from restoration: {e}")

    def test_02_accepts_valid_image_and_returns_expected_keys(self):
        """2 & 3. Verify function accepts valid image and returns expected dictionary keys."""
        from restoration import restore_image

        # Create a synthetic 120x120 3-channel BGR test image
        test_img = np.full((120, 120, 3), 100, dtype=np.uint8)
        # Add a simulated white scratch (intensity 240 > 195 threshold)
        test_img[30:40, 20:80] = 240

        result = restore_image(test_img)

        self.assertIsInstance(result, dict)
        expected_keys = {"original", "grayscale", "threshold", "mask", "restored"}
        self.assertEqual(set(result.keys()), expected_keys)

    def test_03_restored_image_dimensions_and_types(self):
        """4. Verify restored image has valid dimensions and data types."""
        from restoration import restore_image

        h, w = 150, 200
        test_img = np.full((h, w, 3), 120, dtype=np.uint8)
        test_img[50:60, 50:150] = 250  # Scratch

        result = restore_image(test_img)

        self.assertEqual(result["restored"].shape, (h, w, 3))
        self.assertEqual(result["restored"].dtype, np.uint8)
        self.assertEqual(result["original"].shape, (h, w, 3))
        self.assertEqual(result["grayscale"].shape, (h, w))
        self.assertEqual(result["threshold"].shape, (h, w))
        self.assertEqual(result["mask"].shape, (h, w))

    def test_04_damage_mask_validity(self):
        """5. Verify the damage mask is a valid binary mask."""
        from restoration import restore_image

        test_img = np.full((100, 100, 3), 100, dtype=np.uint8)
        # Draw a bright spot
        test_img[45:55, 45:55] = 255

        result = restore_image(test_img)
        mask = result["mask"]

        # Mask should only contain binary values 0 and 255
        unique_vals = set(np.unique(mask))
        self.assertTrue(unique_vals.issubset({0, 255}))
        # The center area should be detected as damaged (white = 255)
        self.assertEqual(mask[50, 50], 255)
        # Far corner should remain background (black = 0)
        self.assertEqual(mask[5, 5], 0)

    def test_05_algorithm_parameters_preserved(self):
        """6. Verify thresholding and dilation parameters match specification."""
        from restoration import restore_image

        # Threshold test: intensity 195 must be 0, intensity 196 must be 255
        test_img = np.zeros((50, 50, 3), dtype=np.uint8)
        test_img[10, 10] = 195  # At or below threshold
        test_img[20, 20] = 196  # Above threshold (195)

        result = restore_image(test_img)
        thresh = result["threshold"]

        self.assertEqual(thresh[10, 10], 0, "Pixel with value 195 should be thresholded to 0")
        self.assertEqual(thresh[20, 20], 255, "Pixel with value 196 should be thresholded to 255")

        # Dilation test: 7x7 kernel with 1 iteration should expand an isolated pixel by 3 in all directions
        mask = result["mask"]
        # Pixel at (20, 20) expanded by 3: (20-3=17) to (20+3=23)
        self.assertEqual(mask[20, 20], 255)
        self.assertEqual(mask[17, 20], 255, "Dilation kernel 7x7 should cover radius of 3")
        self.assertEqual(mask[23, 20], 255, "Dilation kernel 7x7 should cover radius of 3")
        self.assertEqual(mask[16, 20], 0, "Dilation should not exceed kernel radius")

    def test_06_sample_image_restoration(self):
        """Verify restoration operates successfully on real sample assets."""
        from restoration import restore_image

        sample_path = os.path.join(PROJECT_ROOT, "assets", "sample_images", "damaged_05.jpg")
        if os.path.exists(sample_path):
            img = cv2.imread(sample_path)
            self.assertIsNotNone(img, "Failed to read sample image")
            result = restore_image(img)
            self.assertEqual(result["restored"].shape, img.shape)
            self.assertGreater(np.count_nonzero(result["mask"]), 0, "Expected damage detected in sample image")


if __name__ == "__main__":
    unittest.main()
