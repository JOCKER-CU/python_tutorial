# import pdfplumber
# import pandas as pd
# from tabulate import tabulate

# # Step 1: Read the PDF and extract tables
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"
# tables = []

# with pdfplumber.open(pdf_path) as pdf:
#     for page in pdf.pages:
#         tables.extend(page.extract_tables())

# # Step 2: Process each table
# for i, table in enumerate(tables):
#     print(f"Processing Table {i + 1}:")
    
#     # Convert to DataFrame
#     df = pd.DataFrame(table[1:], columns=table[0])
    
#     # Add borders using tabulate
#     bordered_table = tabulate(df, headers='keys', tablefmt='grid')
#     print("\nBordered Table:")
#     print(bordered_table)
    
#     # Export as HTML
#     html_output = df.to_html(index=False, border=1)
#     with open(f"table_{i + 1}.html", "w") as f:
#         f.write(html_output)
    
#     # Export as JSON
#     json_output = df.to_json(orient='records', indent=4)
#     with open(f"table_{i + 1}.json", "w") as f:
#         f.write(json_output)
    
#     print(f"Table {i + 1} exported as HTML and JSON.\n")


#unbordered table 
# import pdfplumber
# import pandas as pd
# import json

# # Step 1: Read the PDF and extract tables
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# with pdfplumber.open(pdf_path) as pdf:
#     tables = []
#     for page in pdf.pages:
#         # Use "lattice" mode for bordered tables (better extraction)
#         page_tables = page.extract_tables(table_settings={"vertical_strategy": "lines", "horizontal_strategy": "lines"})
#         tables.extend(page_tables)

# # Step 2: Process each table
# for i, table in enumerate(tables):
#     print(f"Processing Table {i + 1}:")
    
#     # Convert to DataFrame (keep original structure)
#     if len(table) == 0:
#         print(f"Table {i + 1} is empty. Skipping...")
#         continue
    
#     # Assume the first row is the header
#     df = pd.DataFrame(table[1:], columns=table[0])
    
#     # Export as HTML (preserve original borders)
#     html_output = df.to_html(index=False, border=0, classes="bordered-table")  # Use CSS for styling
#     with open(f"table_{i + 1}.html", "w") as f:
#         f.write(html_output)
    
#     # Export as JSON
#     json_output = df.to_json(orient='records', indent=4)
#     with open(f"table_{i + 1}.json", "w") as f:
#         f.write(json_output)
    
#     print(f"Table {i + 1} exported as HTML and JSON.\n")


# import pdfplumber
# import pandas as pd
# import json

# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # Extract tables with explicit line detection for bordered tables
# with pdfplumber.open(pdf_path) as pdf:
#     tables = []
#     for page in pdf.pages:
#         tables.extend(page.extract_tables(table_settings={
#             "vertical_strategy": "lines",
#             "horizontal_strategy": "lines",
#         }))

# # Process the first table (adjust index if needed)
# table = tables[0]  # Assuming the first table is the target

# # Split raw data into structured key-value pairs
# structured_data = []

# # First row: Header ("Name Gender Age")
# header = table[0][0].split()  # Split into ["Name", "Gender", "Age"]

# # Subsequent rows: Entries like "Policy Owner KHANT TI KYI Male 31"
# for row in table[1:]:
#     entry = row[0].split("\n")  # Split multi-line entries
#     for line in entry:
#         parts = line.split()  # Split into ["Policy", "Owner", "KHANT", ...]
#         if len(parts) >= 4:
#             role = " ".join(parts[:2])  # "Policy Owner" or "Life Insured"
#             name = " ".join(parts[2:-2])  # "KHANT TI KYI"
#             gender = parts[-2]  # "Male"
#             age = parts[-1]  # "31"
#             structured_data.append({
#                 "Customer Information": {
#                     "Role": role,
#                     "Name": name,
#                     "Gender": gender,
#                     "Age": age
#                 }
#             })

# # Convert to JSON
# json_output = json.dumps(structured_data, indent=4)
# print(json_output)

# # Save to file
# with open("customer_info.json", "w") as f:
#     f.write(json_output)


# import pdfplumber
# import json

# def parse_table_dynamically(table):
#     """Parse a table dynamically using the first row as headers."""
#     if not table:
#         return None
    
#     # Extract headers (first row)
#     headers = []
#     for cell in table[0]:
#         if cell is not None:
#             headers.append(cell.strip())
#         else:
#             headers.append("")  # Handle empty headers
    
#     structured = []
#     for row in table[1:]:
#         if not row:  # Skip empty rows
#             continue
        
#         row_data = {}
#         for idx, header in enumerate(headers):
#             # Ensure the row has enough columns and cell is not None
#             if idx < len(row) and row[idx] is not None:
#                 value = row[idx].strip()
#             else:
#                 value = ""  # Default for missing cells
            
#             # Handle multi-line values (e.g., "Policy Owner\nLife Insured")
#             if "\n" in value:
#                 row_data[header] = [v.strip() for v in value.split("\n") if v.strip()]
#             else:
#                 row_data[header] = value
        
#         structured.append(row_data)
    
#     return structured

# def process_pdf(pdf_path):
#     all_tables = {}
    
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_num, page in enumerate(pdf.pages):
#             tables = page.extract_tables(table_settings={
#                 "vertical_strategy": "lines",
#                 "horizontal_strategy": "lines"
#             })
            
#             for table_num, table in enumerate(tables):
#                 parsed = parse_table_dynamically(table)
#                 if parsed:
#                     table_name = f"Page_{page_num + 1}_Table_{table_num + 1}"
#                     all_tables[table_name] = parsed
    
#     return all_tables

# # Example usage
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"
# structured_data = process_pdf(pdf_path)

# # Save to JSON
# with open("dynamic_tables.json", "w") as f:
#     json.dump(structured_data, indent=4, fp=f)

# print("JSON file generated successfully!")


import pdfplumber
import json

def parse_table_dynamically(table):
    """Parse a table dynamically using the first row as headers."""
    if not table:
        return None
    
    # Extract headers (first row)
    headers = []
    for cell in table[0]:
        if cell is not None:
            headers.append(cell.strip())
        else:
            headers.append("")  # Handle empty headers
    
    structured = []
    for row in table[1:]:
        if not row:  # Skip empty rows
            continue
        
        row_data = {}
        for idx, header in enumerate(headers):
            if idx < len(row) and row[idx] is not None:
                value = row[idx].strip()
            else:
                value = ""
            
            if "\n" in value:
                row_data[header] = [v.strip() for v in value.split("\n") if v.strip()]
            else:
                row_data[header] = value
        
        structured.append(row_data)
    
    return structured

def process_pdf(pdf_path):
    all_tables = {}
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages):
            tables = page.extract_tables(table_settings={
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines"
            })
            
            for table_num, table in enumerate(tables):
                parsed = parse_table_dynamically(table)
                if parsed:
                    table_name = f"Page_{page_num + 1}_Table_{table_num + 1}"
                    all_tables[table_name] = parsed
    
    return all_tables

def generate_html(structured_data):
    """Generate an HTML file with styled tables."""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            .data-table {
                border-collapse: collapse;
                width: 100%;
                margin-bottom: 20px;
            }
            .data-table th, .data-table td {
                border: 1px solid #dddddd;
                padding: 8px;
                text-align: left;
            }
            .data-table th {
                background-color: #f2f2f2;
            }
            .data-table tr:nth-child(even) {
                background-color: #f9f9f9;
            }
            h2 {
                color: #333;
                margin-top: 30px;
            }
        </style>
    </head>
    <body>
    """

    for table_name, rows in structured_data.items():
        html += f"<h2>{table_name}</h2>"
        html += '<table class="data-table">'
        
        # Add headers
        if rows:
            html += "<tr>"
            for header in rows[0].keys():
                html += f"<th>{header}</th>"
            html += "</tr>"
        
        # Add rows
        for row in rows:
            html += "<tr>"
            for value in row.values():
                # Handle lists (multi-line values)
                if isinstance(value, list):
                    cell_content = "<br>".join(value)
                else:
                    cell_content = str(value)
                html += f"<td>{cell_content}</td>"
            html += "</tr>"
        
        html += "</table>"
    
    html += "</body></html>"
    return html

# Example usage
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"
structured_data = process_pdf(pdf_path)

# Save to JSON
with open("dynamic_tables.json", "w") as f:
    json.dump(structured_data, indent=4, fp=f)

# Save to HTML
html_output = generate_html(structured_data)
with open("dynamic_tables.html", "w", encoding="utf-8") as f:
    f.write(html_output)

print("JSON and HTML files generated successfully!")