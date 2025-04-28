import cv2
import numpy as np

def run_ela(image_path, quality=90):
    original = cv2.imread(image_path)
    temp_path = image_path.replace(".jpg", "_ela.jpg")

    cv2.imwrite(temp_path, original, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    compressed = cv2.imread(temp_path)

    ela_image = cv2.absdiff(original, compressed)
    ela_gray = cv2.cvtColor(ela_image, cv2.COLOR_BGR2GRAY)

    mean_error = np.mean(ela_gray)
    return mean_error
