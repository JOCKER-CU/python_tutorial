import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    text = ""

    # Iterate through each page
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text("text")  # Extract text in plain format

    return text

# Example usage C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf
pdf_path = r"C:\Users\hanna\Downloads\New-Motor-Insurance-Brochure-MM.pdf"
text = extract_text_from_pdf(pdf_path)
print(text)