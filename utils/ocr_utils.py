import easyocr
import cv2
import numpy as np
from pdf2image import convert_from_path

# Initialize OCR reader once
ocr = easyocr.Reader(['en'], gpu=False)

def extract_text_from_image(img):
    results = ocr.readtext(img)
    extracted_text = " ".join([text[1] for text in results])
    return extracted_text

def convert_pdf_to_images(pdf_path):
    pages = convert_from_path(pdf_path, dpi=300)
    images = [cv2.cvtColor(np.array(p), cv2.COLOR_RGB2BGR) for p in pages]
    return images
