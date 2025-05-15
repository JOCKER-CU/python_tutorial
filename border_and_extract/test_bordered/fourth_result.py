# import pdfplumber
# import json

# def parse_table_dynamically(table):
#     """Parse tables dynamically with robust handling of cells and headers."""
#     if not table or not table[0]:
#         return None
    
#     # Extract headers (clean empty cells)
#     headers = [cell.strip() if cell is not None else "" for cell in table[0]]
    
#     structured = []
#     for row in table[1:]:
#         if not row:
#             continue
        
#         # Pad the row to match header length (fix missing columns)
#         padded_row = list(row) + [""] * (len(headers) - len(row))
#         row_data = {}
        
#         for idx, header in enumerate(headers):
#             cell_value = padded_row[idx].strip() if padded_row[idx] is not None else ""
            
#             # Split multi-line cells into lists
#             if "\n" in cell_value:
#                 row_data[header] = [v.strip() for v in cell_value.split("\n") if v.strip()]
#             else:
#                 row_data[header] = cell_value
        
#         structured.append(row_data)
    
#     return structured

# def process_pdf(pdf_path):
#     all_tables = {}
    
#     with pdfplumber.open(pdf_path) as pdf:
#         for page_num, page in enumerate(pdf.pages):
#             # Enhanced table extraction settings
#             tables = page.extract_tables(table_settings={
#                 "vertical_strategy": "lines",
#                 "horizontal_strategy": "lines",
#                 "explicit_vertical_lines": [],  # Adjust if lines are missing
#                 "explicit_horizontal_lines": [],
#                 "snap_tolerance": 8,           # Merge nearby lines
#                 "join_tolerance": 10,          # Merge text across gaps
#                 "edge_min_length": 15,         # Filter small line fragments
#             })
            
#             for table_num, raw_table in enumerate(tables):
#                 parsed_table = parse_table_dynamically(raw_table)
#                 if parsed_table:
#                     table_name = f"Page_{page_num + 1}_Table_{table_num + 1}"
#                     all_tables[table_name] = parsed_table
    
#     return all_tables

# def generate_html(structured_data):
#     """Generate HTML with strict column alignment and error handling."""
#     html = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <style>
#             .data-table { border-collapse: collapse; width: 100%; margin: 20px 0; }
#             .data-table th, .data-table td { border: 1px solid #ddd; padding: 8px; text-align: left; }
#             .data-table th { background-color: #f2f2f2; }
#             .data-table tr:hover { background-color: #f5f5f5; }
#             h2 { color: #2c3e50; margin-top: 30px; }
#         </style>
#     </head>
#     <body>
#     """
    
#     for table_name, rows in structured_data.items():
#         html += f"<h2>{table_name}</h2>"
#         if not rows:
#             html += "<p>No data found in this table.</p>"
#             continue
        
#         headers = list(rows[0].keys()) if rows else []
#         html += '<table class="data-table"><tr>'
        
#         # Add headers
#         for header in headers:
#             html += f"<th>{header}</th>"
#         html += "</tr>"
        
#         # Add rows (ensure all rows match header count)
#         for row in rows:
#             html += "<tr>"
#             for header in headers:
#                 cell = row.get(header, "")
#                 if isinstance(cell, list):
#                     cell = "<br>".join(cell)
#                 html += f"<td>{cell}</td>"
#             html += "</tr>"
        
#         html += "</table>"
    
#     html += "</body></html>"
#     return html

# # Example usage
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"
# structured_data = process_pdf(pdf_path)

# # Save outputs
# with open("refined_tables.json", "w") as f:
#     json.dump(structured_data, indent=4, fp=f)

# html_output = generate_html(structured_data)
# with open("refined_tables.html", "w", encoding="utf-8") as f:
#     f.write(html_output)

# print("Refined JSON and HTML files generated!")

import pdfplumber
import json
from collections import defaultdict

def extract_tables(pdf_path):
    """Extract tables with enhanced border detection and text merging"""
    all_tables = defaultdict(list)
    
    with pdfplumber.open(pdf_path) as pdf:
        for page_num, page in enumerate(pdf.pages, 1):
            tables = page.extract_tables({
                "vertical_strategy": "lines",
                "horizontal_strategy": "lines",
                "snap_tolerance": 10,
                "join_tolerance": 15,
                "edge_min_length": 10,
            })
            
            for table_num, table in enumerate(tables, 1):
                print(f"Processing Page {page_num}, Table {table}")
                if table:
                    cleaned_table = clean_table(table)
                    if cleaned_table:
                        all_tables[(page_num, table_num)] = cleaned_table
                
    return all_tables

def clean_table(table):
    """Clean and normalize table data"""
    # Remove empty rows
    cleaned = []
    for row in table:
        # cell.strip() if cell is not None else ""
        cleaned_row = [cell.strip() if cell is not None else "" for cell in row]
        if any(cleaned_row):
            cleaned.append(cleaned_row)
    
    if not cleaned:
        return []
    
    # Pad rows to equal length
    max_cols = max(len(row) for row in cleaned)
    padded = [row + [""] * (max_cols - len(row)) for row in cleaned]
    
    # Transpose and filter empty columns
    transposed = list(zip(*padded))
    filtered_cols = [col for col in transposed if any(cell.strip() for cell in col)]
    
    return list(zip(*filtered_cols)) if filtered_cols else []

def process_table_data(raw_tables):
    """Process all raw tables into structured format"""
    processed = {}
    for (page, table_num), table_data in raw_tables.items():
        if not table_data:
            continue
            
        # Detect headers (first non-empty row)
        headers = table_data[0]
        rows = []
        
        for row in table_data[1:]:
            row_data = {}
            for idx, header in enumerate(headers):
                if idx < len(row):
                    value = row[idx].strip()
                    row_data[header] = value if value else ""
            rows.append(row_data)
        
        processed[f"Page_{page}_Table_{table_num}"] = {
            "headers": headers,
            "rows": rows
        }
    return processed

def generate_html_output(tables_data):
    """Generate HTML report with tables"""
    html = """<!DOCTYPE html>
<html>
<head>
    <style>
        table { border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
"""
    
    for table_key, data in tables_data.items():
        html += f"<h2>{table_key}</h2>\n"
        html += "<table>\n"
        html += "  <tr>\n"
        for header in data["headers"]:
            html += f"    <th>{header}</th>\n"
        html += "  </tr>\n"
        
        for row in data["rows"]:
            html += "  <tr>\n"
            for header in data["headers"]:
                value = row.get(header, "")
                html += f"    <td>{value}</td>\n"
            html += "  </tr>\n"
        html += "</table>\n"
    
    html += "</body>\n</html>"
    return html

def main(pdf_path):
    # Extract tables
    raw_tables = extract_tables(pdf_path)
    
    # Process tables
    processed_tables = process_table_data(raw_tables)
    
    # Generate JSON
    with open("output.json", "w") as f:
        json.dump(processed_tables, f, indent=2)
    
    # Generate HTML
    html = generate_html_output(processed_tables)
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)
    
    print("Processing completed. Output files created: output.json and output.html")

# Set your PDF file path here
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# Execute the program
if __name__ == "__main__":
    main(pdf_path)