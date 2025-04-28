from fuzzywuzzy import fuzz

# Predefined valid certificates (You can connect a database instead later)
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

    # Check: At least 3 important keywords + text length > 100
    if len(keyword_matches) >= 3 and len(extracted_text) >= 100:
        return True
    else:
        return False
