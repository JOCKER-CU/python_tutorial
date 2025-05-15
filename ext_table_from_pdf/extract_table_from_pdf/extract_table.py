# import cv2
# import numpy as np
# import pytesseract
# from pdf2image import convert_from_path
# from PIL import Image

# def preprocess_image(image):
#     """Enhance image for better OCR results."""
#     gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
#     thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
#     return thresh

# def extract_table_from_image(image):
#     """Extract structured table data using OCR and coordinates."""
#     # Preprocess the image
#     processed_img = preprocess_image(image)
    
#     # Use Tesseract to get text with coordinates
#     data = pytesseract.image_to_data(
#         processed_img, output_type=pytesseract.Output.DICT, config="--psm 6"
#     )
    
#     # Group text by rows (y-coordinates)
#     rows = {}
#     for i in range(len(data["text"])):
#         if int(data["conf"][i]) > 60:  # Confidence threshold
#             y = data["top"][i]
#             text = data["text"][i].strip()
#             if text:
#                 # Group by approximate row (using y ± 5 pixels tolerance)
#                 row_key = (y // 10) * 10  # Adjust tolerance as needed
#                 if row_key not in rows:
#                     rows[row_key] = []
#                 rows[row_key].append((data["left"][i], text))
    
#     # Sort rows and columns to reconstruct the table
#     table = []
#     for y in sorted(rows.keys()):
#         # Sort columns by x-coordinate
#         columns = sorted(rows[y], key=lambda x: x[0])
#         row_data = [text for (x, text) in columns]
#         table.append(row_data)
    
#     return table

# def extract_tables_from_scanned_pdf(pdf_path):
#     """Convert PDF pages to images and process each image."""
#     images = convert_from_path(pdf_path, dpi=300)  # Adjust DPI for clarity
#     all_tables = []
#     for image in images:
#         table = extract_table_from_image(image)
#         if table:
#             all_tables.extend(table)
#     return all_tables

# # Example usage
# tables = extract_tables_from_scanned_pdf(r"C:\Users\hanna\Downloads\Documents\css.pdf")
# print("Extracted Tables:", tables)


import pdfplumber

def extract_tables_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        tables = []
        for page in pdf.pages:
            # Extract table(s) from the page
            table = page.extract_table()
            if table:
                tables.extend(table)
        return tables

# Example usage
tables = extract_tables_from_pdf(r"C:\Users\hanna\Downloads\Documents\css.pdf")
print("Extracted Tables:", tables)