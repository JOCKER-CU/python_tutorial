import tabula
import pandas as pd
import os

# Path to the PDF file
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# Directory to save HTML files
html_dir = "html_tables"
if not os.path.exists(html_dir):
    os.makedirs(html_dir)

# Extract tables from the PDF
tables = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

# Save each table as an HTML file
for i, table in enumerate(tables):
    try:
        # Define the HTML file path
        html_path = os.path.join(html_dir, f"table_{i + 1}.html")
        
        # Save the table as an HTML file
        table.to_html(html_path, index=False)
        print(f"Table {i + 1} saved as {html_path}")
    except Exception as e:
        print(f"Error processing Table {i + 1}: {e}")

# Alternatively, save all tables into a single HTML file
all_tables_path = os.path.join(html_dir, "all_tables.html")
with open(all_tables_path, "w", encoding="utf-8") as file:
    for i, table in enumerate(tables):
        file.write(f"<h2>Table {i + 1}</h2>\n")  # Add a header for each table
        file.write(table.to_html(index=False))  # Convert the table to HTML and write to file
        file.write("\n\n")  # Add spacing between tables
print(f"All tables saved as {all_tables_path}")