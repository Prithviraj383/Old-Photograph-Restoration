
import cv2
import numpy as np


def restore_image(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Generate binary damage mask
    _, threshold = cv2.threshold(
        gray, 195, 255, cv2.THRESH_BINARY
    )

    # Dilate the mask
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.dilate(
        threshold, kernel, iterations=1
    )

    # Restore damaged regions
    restored = cv2.inpaint(
        image, mask, 4, cv2.INPAINT_TELEA
    )

    return {
        "original": image,
        "grayscale": gray,
        "threshold": threshold,
        "mask": mask,
        "restored": restored
    }