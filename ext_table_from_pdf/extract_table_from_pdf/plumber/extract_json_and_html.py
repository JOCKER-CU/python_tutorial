import pdfplumber
import json
import pandas as pd
import os

def extract_tables_from_pdf(pdf_path):
    tables_by_page = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):  # Start page numbering from 1
            # Extract table(s) from the page
            table = page.extract_table()
            if table:
                tables_by_page[page_number] = table
    return tables_by_page

def save_tables_as_json(tables_by_page, json_path):
    """Save tables as a JSON file."""
    with open(json_path, "w") as json_file:
        json.dump(tables_by_page, json_file, indent=4)
    print(f"Tables saved as JSON: {json_path}")

def save_tables_as_html(tables_by_page, html_dir):
    """Save tables as HTML files (one per page)."""
    # Create the directory if it doesn't exist
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    for page_number, table in tables_by_page.items():
        try:
            # Find the maximum number of columns in the table
            max_columns = max(len(row) for row in table)

            # Adjust the header to match the maximum number of columns
            header = table[0] if table else []
            header = header + [f"Column_{i}" for i in range(len(header), max_columns)]

            # Adjust data rows to match the maximum number of columns
            adjusted_table = []
            for row in table:
                adjusted_row = row + [None] * (max_columns - len(row))  # Fill missing columns with None
                adjusted_table.append(adjusted_row)

            # Convert the adjusted table data into a pandas DataFrame
            df = pd.DataFrame(adjusted_table[1:], columns=header)

            # Save the DataFrame as an HTML file
            html_path = os.path.join(html_dir, f"page_{page_number}.html")
            df.to_html(html_path, index=False)
            print(f"Tables for Page {page_number} saved as HTML: {html_path}")
        except Exception as e:
            print(f"Error processing Page {page_number}: {e}")

# Example usage  C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf, C:\Users\hanna\Downloads\Insurance Claim Form 1.pdf
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"  # Replace with your PDF file path
json_path = "tables_by_page.json"  # Path to save JSON file
html_dir = "border_html_tables_Insurance_SALES-ILLUSTRATION-LIFEPRO"  # Directory to save HTML files

# Extract tables from PDF
tables_by_page = extract_tables_from_pdf(pdf_path)

# Save tables as JSON
save_tables_as_json(tables_by_page, json_path)

# Print the extracted tables
for page_number, table in tables_by_page.items():
    print(f"Page {page_number}:")
    for row in table:
        print(row)

# Save tables as HTML
save_tables_as_html(tables_by_page, html_dir)