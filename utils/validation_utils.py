from fuzzywuzzy import fuzz
from .google_utils import validate_with_gemini

# Predefined valid certificates
valid_certificates = {
    "John Doe": "CERT12345",
    "Jane Smith": "CERT67890",
    "Alice Johnson": "CERT11111"
}

def validate_extracted_text(extracted_text):
    important_keywords = [
        "Certificate", "certification", "participated", "completion",
        "Microsoft", "NASSCOM", "Coursera", "Google", "achievement",
        "presented to", "awarded to", "completion of", "successfully completed"
    ]

    extracted_text_lower = extracted_text.lower()
    keyword_matches = [kw.lower() for kw in important_keywords if kw.lower() in extracted_text_lower]

    # Simple heuristic check
    passed_heuristic = len(keyword_matches) >= 3 and len(extracted_text) >= 100

    # Gemini AI response
    gemini_response = validate_with_gemini(extracted_text)

    # Final result
    return {
        "passed_heuristic": passed_heuristic,
        "gemini_feedback": gemini_response
    }
