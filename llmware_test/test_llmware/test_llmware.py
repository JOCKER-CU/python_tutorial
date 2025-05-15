# from llmware.parsers import Parser
# import json

# # Function to convert a table to HTML
# def table_to_html(table):
#     html = "<table border='1'>\n"
#     for row in table:
#         html += "  <tr>\n"
#         for cell in row:
#             html += f"    <td>{cell}</td>\n"
#         html += "  </tr>\n"
#     html += "</table>"
#     return html

# # Path to your PDF file
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # Initialize the Parser
# parser = Parser()

# # Parse the PDF
# parsed_data = parser.parse_pdf(pdf_path)

# # Extract tables from the parsed data
# tables = []
# for page in parsed_data:
#     if "tables" in page:
#         tables.extend(page["tables"])

# # Save tables as JSON
# json_output = {"tables": tables}
# with open("extracted_tables.json", "w") as json_file:
#     json.dump(json_output, json_file, indent=4)
# print("Tables saved to 'extracted_tables.json'")

# # Save tables as HTML
# html_output = "<html><body>\n"
# for i, table in enumerate(tables):
#     html_output += f"<h2>Table {i+1}</h2>\n"
#     html_output += table_to_html(table)
#     print(table)
# html_output += "</body></html>"

# with open("extracted_tables.html", "w") as html_file:
#     html_file.write(html_output)
# print("Tables saved to 'extracted_tables.html'")


from llmware.parsers import Parser
import json
from pdf2image import convert_from_path
import pytesseract

# Function to convert a table to HTML
def table_to_html(table):
    html = "<table border='1'>\n"
    for row in table:
        html += "  <tr>\n"
        for cell in row:
            html += f"    <td>{cell}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html

# Function to extract text from PDF using OCR
def extract_text_with_ocr(pdf_path):
    images = convert_from_path(pdf_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

# Path to your PDF file
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# Initialize the Parser
parser = Parser()

# Check if the PDF is image-based
try:
    # Try parsing the PDF directly
    print("Attempting to parse the PDF directly...")
    parsed_data = parser.parse_pdf(pdf_path)
    print("PDF parsed successfully.")
    print("Parsed data structure:", parsed_data)  # Debug: Print parsed data
except Exception as e:
    print("PDF parsing failed. Attempting OCR...")
    # Extract text using OCR
    text = extract_text_with_ocr(pdf_path)
    print("OCR text extracted:", text[:500])  # Debug: Print first 500 characters of OCR text
    # Save the extracted text to a file (for debugging)
    with open("extracted_text.txt", "w") as text_file:
        text_file.write(text)
    # Manually process the text to extract tables (if needed)
    tables = []  # Replace this with your logic to extract tables from text
else:
    # Extract tables from the parsed data
    tables = []
    for page in parsed_data:
        if "tables" in page:
            tables.extend(page["tables"])
    print("Tables extracted:", tables)  # Debug: Print extracted tables

# Save tables as JSON
json_output = {"tables": tables}
with open("extracted_tables.json", "w") as json_file:
    json.dump(json_output, json_file, indent=4)
print("Tables saved to 'extracted_tables.json'")

# Save tables as HTML
html_output = "<html><body>\n"
for i, table in enumerate(tables):
    html_output += f"<h2>Table {i+1}</h2>\n"
    html_output += table_to_html(table)
    print(table)
html_output += "</body></html>"

with open("extracted_tables.html", "w") as html_file:
    html_file.write(html_output)
print("Tables saved to 'extracted_tables.html'")