# Certificate Detection & Verification Web App

This project is a Flask-based web application for verifying the authenticity of certificates (images or PDFs). It uses OCR (Optical Character Recognition), ELA (Error Level Analysis), and text validation to detect fake or tampered certificates.

---

## Features

- **Upload Certificate**: Supports both image and PDF certificate uploads.
- **OCR Extraction**: Extracts text from certificates using EasyOCR.
- **Forgery Detection**: Uses Error Level Analysis (ELA) to detect possible image tampering.
- **Text Validation**: Checks for the presence of important keywords and validates the extracted text.
- **User-Friendly Interface**: Clean UI with light/dark mode toggle.
- **Result Summary**: Shows extracted text, forgery score, and verdict.

---

## Project Structure
certificate_detection/ │ ├── app.py # Main Flask application ├── requirements.txt # Python dependencies ├── static/ │ └── styles.css # CSS styles ├── templates/ │ ├── index.html # Upload form page │ └── result.html # Result display page ├── utils/ │ ├── ela_utils.py # Error Level Analysis utilities │ ├── ocr_utils.py # OCR and PDF-to-image utilities │ └── validation_utils.py # Text validation logic ├── temp/ # Temporary storage for uploads └── models/ # (Optional) ML models (e.g., font_classifier.h5)

---

## Endpoints

| Endpoint      | Method | Description                                  |
|---------------|--------|----------------------------------------------|
| `/`           | GET    | Home page with upload form                   |
| `/verify`     | POST   | Handles certificate upload and verification  |
| `/static/...` | GET    | Serves static files (CSS, images, etc.)      |

### Endpoint Details

- **`/`**  
  Renders the [index.html](certificate_detection/templates/index.html) upload form.

- **`/verify`**  
  Accepts a file upload (image or PDF), processes it, and renders [result.html](certificate_detection/templates/result.html) with:
  - Extracted text
  - Forgery detection result (mean error, verdict)
  - Text validation status

---

## How It Works

1. **User uploads a certificate** (image or PDF) via the web form.
2. **OCR Extraction**:  
   - If PDF, each page is converted to an image.
   - Text is extracted from each image using EasyOCR ([`extract_text_from_image`](certificate_detection/utils/ocr_utils.py)).
3. **Forgery Detection**:  
   - ELA is run on the image ([`run_ela`](certificate_detection/utils/ela_utils.py)).
   - If mean error > 8, possible forgery is flagged.
4. **Text Validation**:  
   - Checks for important keywords and minimum text length ([`validate_extracted_text`](certificate_detection/utils/validation_utils.py)).
5. **Result Display**:  
   - Verdict is shown: Genuine, Suspicious, or Fake.
   - All details are displayed on the result page.

---

### Prerequisites

- Python 3.7+
- pip

### Installation Steps

1. **Clone the repository**
   ```sh
   git clone <repo-url>
   cd certificate_detection
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Run the application**
   ```sh
   python app.py
   ```
4. **Access the web app**
   - Open a browser and go to `http://127.0.0.1:5000`.

---

## Usage

1. On the home page, upload a certificate file (image or PDF).
2. Click on the "Verify" button.
3. Wait for the analysis to complete.
4. Review the results on the displayed result page.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make the necessary changes and commit them.
4. Push your branch to your forked repository.
5. Create a pull request describing your changes.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Inspired by the need to verify digital certificates' authenticity.
- Leveraged existing technologies: Flask, EasyOCR, OpenCV, and more.
- Thanks to all contributors and supporters.

---
