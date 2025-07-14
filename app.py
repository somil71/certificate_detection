from flask import Flask, request, jsonify, send_from_directory, render_template
import os
import cv2
import numpy as np
from utils.ocr_utils import extract_text_from_image, convert_pdf_to_images
from utils.validation_utils import validate_extracted_text
from utils.ela_utils import run_ela

# App Setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'temp'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify_certificate():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filename)

    # Determine if PDF or Image
    if filename.lower().endswith('.pdf'):
        images = convert_pdf_to_images(filename)
    else:
        img = cv2.imread(filename)
        images = [img]

    results = []
    for img in images:
        extracted_text = extract_text_from_image(img) or ""
        temp_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image.jpg')
        cv2.imwrite(temp_image_path, img)
        mean_error = run_ela(temp_image_path)
        forgery_detected = mean_error > 8  # Stricter threshold now
    
        validation_result = validate_extracted_text(extracted_text)
        heuristic_pass = validation_result["passed_heuristic"]
        gemini_feedback = validation_result["gemini_feedback"]

    
        if heuristic_pass and not forgery_detected:
        
            verdict = "Genuine"
        elif heuristic_pass and forgery_detected:
            verdict = "Suspicious (Possible Forgery)"
        else:
            verdict = "Fake (Text validation failed)"
            
        result = {
            "extracted_text": extracted_text,
            "heuristic_pass": heuristic_pass,
            "gemini_feedback": gemini_feedback,
            "forgery_mean_error": round(float(mean_error), 3),
            "forgery_detected": forgery_detected,
            "verdict": verdict
        }

    
        results.append(result)
    
    return render_template('result.html', results=results)



if __name__ == '__main__':
    app.run(debug=True)
