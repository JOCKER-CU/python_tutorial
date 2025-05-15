import pytesseract
from pdf2image import convert_from_path
import os

# Set the path to the Tesseract executable (if not in PATH)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image_based_pdf(pdf_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    # Extract text from each image using OCR
    extracted_text = ""
    for i, image in enumerate(images):
        print(f"Processing page {i + 1}...")
        text = pytesseract.image_to_string(image, lang='tha')  # Use 'tha' for Thai language
        extracted_text += f"===== Page {i + 1} =====\n{text}\n\n"

    return extracted_text

# Example usage
pdf_path = r"C:\Users\hanna\Downloads\New-Motor-Insurance-Brochure-MM.pdf"
text = extract_text_from_image_based_pdf(pdf_path)

# Save the extracted text to a file
output_file = "extracted_text.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Text extracted and saved to {output_file}")