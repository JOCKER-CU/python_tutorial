# import pdfplumber
# import json
# import pandas as pd

# def extract_tables_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             # Extract table(s) from the page
#             table = page.extract_table()
#             if table:
#                 tables.extend(table)
#         return tables

# def save_tables_as_json(tables, json_path):
#     """Save tables as a JSON file."""
#     with open(json_path, "w") as json_file:
#         json.dump(tables, json_file, indent=4)
#     print(f"Tables saved as JSON: {json_path}")

# def save_tables_as_html(tables, html_path):
#     """Save tables as an HTML file."""
#     # Convert the table data into a pandas DataFrame
#     df = pd.DataFrame(tables[1:], columns=tables[0])  # Assume first row is the header
#     # Save the DataFrame as an HTML file
#     df.to_html(html_path, index=False)
#     print(f"Tables saved as HTML: {html_path}")

# # Example usage
# pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"  # Replace with your PDF file path
# json_path = "tables.json"  # Path to save JSON file
# html_path = "tables.html"  # Path to save HTML file

# # Extract tables from PDF
# tables = extract_tables_from_pdf(pdf_path)

# # Save tables as JSON
# save_tables_as_json(tables, json_path)

# # Save tables as HTML
# save_tables_as_html(tables, html_path)

# print("Extracted Tables:", tables)


# get json and html formats
# import pdfplumber
# import json
# import pandas as pd

# def extract_tables_from_pdf(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         tables = []
#         for page in pdf.pages:
#             # Extract table(s) from the page
#             table = page.extract_table()
#             if table:
#                 tables.extend(table)
#         return tables

# def save_tables_as_json(tables, json_path):
#     """Save tables as a JSON file."""
#     with open(json_path, "w") as json_file:
#         json.dump(tables, json_file, indent=4)
#     print(f"Tables saved as JSON: {json_path}")

# def save_tables_as_html(tables, html_path):
#     """Save tables as an HTML file."""
#     # Find the maximum number of columns in the table
#     max_columns = max(len(row) for row in tables)

#     # Adjust the header to match the maximum number of columns
#     header = tables[0] if tables else []
#     header = header + [f"Column_{i}" for i in range(len(header), max_columns)]

#     # Adjust data rows to match the maximum number of columns
#     adjusted_tables = []
#     for row in tables:
#         adjusted_row = row + [None] * (max_columns - len(row))  # Fill missing columns with None
#         adjusted_tables.append(adjusted_row)

#     # Convert to DataFrame
#     df = pd.DataFrame(adjusted_tables[1:], columns=header)

#     # Save the DataFrame as an HTML file
#     df.to_html(html_path, index=False)
#     print(f"Tables saved as HTML: {html_path}")

# # Example usage
# pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"  # Replace with your PDF file path
# json_path = "tables.json"  # Path to save JSON file
# html_path = "tables.html"  # Path to save HTML file

# # Extract tables from PDF
# tables = extract_tables_from_pdf(pdf_path)

# # Save tables as JSON
# save_tables_as_json(tables, json_path)

# # Save tables as HTML
# save_tables_as_html(tables, html_path)

# print("Extracted Tables:", tables)



# import pdfplumber
# import json
# import pandas as pd
# import os

# def extract_tables_from_pdf(pdf_path):
#     tables_by_page = {}
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_number, page in enumerate(pdf.pages, start=1):  # Start page numbering from 1
#             # Extract table(s) from the page
#             table = page.extract_table()
#             if table:
#                 tables_by_page[page_number] = table
#     return tables_by_page

# def save_tables_as_json(tables_by_page, json_path):
#     """Save tables as a JSON file."""
#     with open(json_path, "w") as json_file:
#         json.dump(tables_by_page, json_file, indent=4)
#     print(f"Tables saved as JSON: {json_path}")

# def save_tables_as_html(tables_by_page, html_dir):
#     """Save tables as HTML files (one per page)."""
#     # Create the directory if it doesn't exist
#     if not os.path.exists(html_dir):
#         os.makedirs(html_dir)

#     for page_number, table in tables_by_page.items():
#         try:
#             # Find the maximum number of columns in the table
#             max_columns = max(len(row) for row in table)

#             # Adjust the header to match the maximum number of columns
#             header = table[0] if table else []
#             header = header + [f"Column_{i}" for i in range(len(header), max_columns)]

#             # Adjust data rows to match the maximum number of columns
#             adjusted_table = []
#             for row in table:
#                 adjusted_row = row + [None] * (max_columns - len(row))  # Fill missing columns with None
#                 adjusted_table.append(adjusted_row)

#             # Convert the adjusted table data into a pandas DataFrame
#             df = pd.DataFrame(adjusted_table[1:], columns=header)

#             # Save the DataFrame as an HTML file
#             html_path = os.path.join(html_dir, f"page_{page_number}.html")
#             df.to_html(html_path, index=False)
#             print(f"Tables for Page {page_number} saved as HTML: {html_path}")
#         except Exception as e:
#             print(f"Error processing Page {page_number}: {e}")

# # Example usage
# pdf_path = r"C:\Users\hanna\Downloads\YaRN.pdf"  # Replace with your PDF file path
# json_path = "tables_by_page.json"  # Path to save JSON file
# html_dir = "html_tables"  # Directory to save HTML files

# # Extract tables from PDF
# tables_by_page = extract_tables_from_pdf(pdf_path)

# # Save tables as JSON
# save_tables_as_json(tables_by_page, json_path)

# # Print the extracted tables
# for page_number, table in tables_by_page.items():
#     print(f"Page {page_number}:")
#     for row in table:
#         print(row)

# # Save tables as HTML
# save_tables_as_html(tables_by_page, html_dir)


import pdfplumber
import json
import pandas as pd
import os

def extract_unbordered_tables_from_pdf(pdf_path):
    tables_by_page = {}
    with pdfplumber.open(pdf_path) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):  # Start page numbering from 1
            # Extract words from the page
            words = page.extract_words(x_tolerance=2, y_tolerance=2)  # Adjust tolerance as needed

            # Group words into rows based on their y-coordinates
            rows = {}
            for word in words:
                y = word["top"]
                row_key = round(y)  # Group words by their y-coordinate
                if row_key not in rows:
                    rows[row_key] = []
                rows[row_key].append((word["x0"], word["text"]))

            # Sort rows by y-coordinate and columns by x-coordinate
            sorted_rows = sorted(rows.keys())
            table = []
            for row_key in sorted_rows:
                # Sort columns by x-coordinate
                columns = sorted(rows[row_key], key=lambda x: x[0])
                row_data = [text for (x, text) in columns]
                table.append(row_data)

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
html_dir = "html_tables_for_SALES-ILLUSTRATION-LIFEPRO"  # Directory to save HTML files

# Extract unbordered tables from PDF
tables_by_page = extract_unbordered_tables_from_pdf(pdf_path)

# Save tables as JSON
save_tables_as_json(tables_by_page, json_path)

# Print the extracted tables
for page_number, table in tables_by_page.items():
    print(f"Page {page_number}:")
    for row in table:
        print(row)

# Save tables as HTML
save_tables_as_html(tables_by_page, html_dir)