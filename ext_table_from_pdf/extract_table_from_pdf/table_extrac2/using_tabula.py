# import json
# import pandas as pd
# import os
# import tabula

# def extract_tables_from_pdf(pdf_path):
#     """
#     Extract tables from a PDF using Tabula.
#     Returns a dictionary where keys are page numbers and values are lists of tables (DataFrames).
#     """
#     tables_by_page = {}
    
#     # Extract tables from all pages
#     tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    
#     # Group tables by page number
#     for i, table in enumerate(tables):
#         page_number = i + 1  # Tabula returns tables in order, so we assume page numbers start from 1
#         if page_number not in tables_by_page:
#             tables_by_page[page_number] = []
#         tables_by_page[page_number].append(table)
    
#     return tables_by_page

# def save_tables_as_json(tables_by_page, json_path):
#     """Save tables as a JSON file."""
#     # Convert DataFrames to dictionaries for JSON serialization
#     tables_dict = {
#         page_number: [table.to_dict(orient="records") for table in tables]
#         for page_number, tables in tables_by_page.items()
#     }
    
#     with open(json_path, "w") as json_file:
#         json.dump(tables_dict, json_file, indent=4)
#     print(f"Tables saved as JSON: {json_path}")

# def save_tables_as_html(tables_by_page, html_dir):
#     """Save tables as HTML files (one per page)."""
#     # Create the directory if it doesn't exist
#     if not os.path.exists(html_dir):
#         os.makedirs(html_dir)

#     for page_number, tables in tables_by_page.items():
#         for table_index, table in enumerate(tables):
#             try:
#                 # Save the DataFrame as an HTML file
#                 html_path = os.path.join(html_dir, f"page_{page_number}_table_{table_index + 1}.html")
#                 table.to_html(html_path, index=False)
#                 print(f"Table {table_index + 1} for Page {page_number} saved as HTML: {html_path}")
#             except Exception as e:
#                 print(f"Error processing Table {table_index + 1} on Page {page_number}: {e}")

# # Example usage
# pdf_path = r"C:\Users\hanna\Downloads\YaRN.pdf"  # Replace with your PDF file path
# json_path = "tables_by_page.json"  # Path to save JSON file
# html_dir = "html_tables_for_test_pdf"  # Directory to save HTML files

# # Extract tables from PDF
# tables_by_page = extract_tables_from_pdf(pdf_path)

# # Save tables as JSON
# save_tables_as_json(tables_by_page, json_path)

# # Print the extracted tables
# for page_number, tables in tables_by_page.items():
#     print(f"Page {page_number}:")
#     for table in tables:
#         print(table)

# # Save tables as HTML
# save_tables_as_html(tables_by_page, html_dir)


import json
import pandas as pd
import os
import tabula

def extract_content_from_pdf(pdf_path):
    """
    Extract both text and tables from a PDF using Tabula and PyMuPDF (fitz).
    Returns a dictionary with text and tables for each page.
    """
    import fitz  # PyMuPDF

    content_by_page = {}

    # Extract text using PyMuPDF
    with fitz.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            content_by_page[page_number] = {"text": page.get_text(), "tables": []}

    # Extract tables using Tabula
    tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)
    for i, table in enumerate(tables):
        page_number = i + 1  # Tabula returns tables in order, so we assume page numbers start from 1
        if page_number in content_by_page:
            content_by_page[page_number]["tables"].append(table)

    return content_by_page

def save_content_as_json(content_by_page, json_path):
    """Save content (text and tables) as a JSON file."""
    # Convert DataFrames to dictionaries for JSON serialization
    content_dict = {
        page_number: {
            "text": content["text"],
            "tables": [table.to_dict(orient="records") for table in content["tables"]]
        }
        for page_number, content in content_by_page.items()
    }

    with open(json_path, "w") as json_file:
        json.dump(content_dict, json_file, indent=4)
    print(f"Content saved as JSON: {json_path}")

def save_tables_as_html(content_by_page, html_dir):
    """Save tables as HTML files (one per page)."""
    # Create the directory if it doesn't exist
    if not os.path.exists(html_dir):
        os.makedirs(html_dir)

    for page_number, content in content_by_page.items():
        for table_index, table in enumerate(content["tables"]):
            try:
                # Save the DataFrame as an HTML file
                html_path = os.path.join(html_dir, f"page_{page_number}_table_{table_index + 1}.html")
                table.to_html(html_path, index=False)
                print(f"Table {table_index + 1} for Page {page_number} saved as HTML: {html_path}")
            except Exception as e:
                print(f"Error processing Table {table_index + 1} on Page {page_number}: {e}")

# Example usage "C:\Users\hanna\Downloads\postgresql-15-US.pdf" C:\Users\hanna\Downloads\YaRN.pdf
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"  # Replace with your PDF file path
json_path = "content_by_page.json"  # Path to save JSON file
html_dir = "html_tables_for_SALES-ILLUSTRATION-LIFEPRO"  # Directory to save HTML files

# Extract content from PDF
content_by_page = extract_content_from_pdf(pdf_path)

# Save content as JSON
save_content_as_json(content_by_page, json_path)

# Print the extracted content
for page_number, content in content_by_page.items():
    print(f"Page {page_number}:")
    print("Text:")
    print(content["text"])
    print("Tables:")
    for table in content["tables"]:
        print(table)

# Save tables as HTML
save_tables_as_html(content_by_page, html_dir)