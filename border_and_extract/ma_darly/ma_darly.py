import pdfplumber
import camelot
import pandas as pd
import os
import json
  # For Google Colab
 
def extract_tables_with_pdfplumber(pdf_path):
    """Extract tables using pdfplumber (works well for tables with borders)."""
    tables_by_page = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            table = page.extract_table()
            if table:
                tables_by_page[page_number] = table
    return tables_by_page
 
def extract_tables_with_camelot(pdf_path):
    """Extract tables using camelot (works well for tables without borders)."""
    tables = camelot.read_pdf(pdf_path, pages='all', flavor='stream')
    tables_by_page = {}
    for i, table in enumerate(tables):
        tables_by_page[i + 1] = table.df.values.tolist()
    return tables_by_page
 
def save_tables_as_html(tables_by_page, output_dir):
    """Save tables as HTML files, adding border="1" to all tables."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
 
    for page_number, table in tables_by_page.items():
        try:
            # Convert the table data into a pandas DataFrame
            df = pd.DataFrame(table[1:], columns=table[0])
 
            # Save the DataFrame as an HTML file
            html_path = os.path.join(output_dir, f"page_{page_number}.html")
            html_table = tabulate(df, headers='keys', tablefmt='html')
 
            # Add border=1 to the table tag
            html_table = html_table.replace('<table>', '<table border="1">')
 
            with open(html_path, 'w') as f:
                f.write(html_table)
            print(f"Tables for Page {page_number} saved as HTML: {html_path}")
        except Exception as e:
            print(f"Error processing Page {page_number}: {e}")
 
def print_tables_as_json(tables_by_page, table_type):
    """Print tables in JSON format."""
    print(f"Tables ({table_type}) in JSON format:")
    print(json.dumps(tables_by_page, indent=4))
 
def process_pdf(pdf_path, output_dir):
    """Process PDF to extract tables with and without borders."""
    # Extract tables with borders using pdfplumber
    tables_with_borders = extract_tables_with_pdfplumber(pdf_path)
    print_tables_as_json(tables_with_borders, "with borders")
    save_tables_as_html(tables_with_borders, os.path.join(output_dir, "with_borders"))
 
    # Extract tables without borders using camelot
    tables_without_borders = extract_tables_with_camelot(pdf_path)
    print_tables_as_json(tables_without_borders, "without borders")
    save_tables_as_html(tables_without_borders, os.path.join(output_dir, "without_borders"))
 
    print(f"Processing complete. Check {output_dir} for the results.")
 
 
# Example usage
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"  # Replace with your PDF file path
output_dir = "ma_darly"  # Directory to save HTML files
  
# Process the PDF
process_pdf(pdf_path, output_dir)