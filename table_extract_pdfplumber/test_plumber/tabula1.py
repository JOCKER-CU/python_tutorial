# from tabula import read_pdf

# # Read tables from a PDF file
# tables = read_pdf(r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf", pages="all", multiple_tables=True, pandas_options={"header": None})

# # Loop through and print each table
# for i, table in enumerate(tables):
#     print(f"Table {i+1}:\n{table}\n")
#     # Save to CSV
#     table.to_csv(f"table_{i+1}.csv", index=False)

from tabula import read_pdf
import pandas as pd

# Specify the PDF file
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# Extract all tables from the PDF
tables = read_pdf(pdf_path, pages="all", multiple_tables=True, pandas_options={"header": None})

# Initialize a counter for unbordered tables
unbordered_table_count = 0

# Loop through and analyze each table
for i, table in enumerate(tables):
    # Custom logic to identify unbordered tables
    # For example, check for missing/empty rows or irregular column counts
    if table.isnull().values.any() or table.shape[1] > 3:  # Example condition
        unbordered_table_count += 1
        # Save the unbordered table to an Excel file
        excel_filename = f"unbordered_table_{unbordered_table_count}.xlsx"
        table.to_excel(excel_filename, index=False, header=False)
        print(f"Unbordered Table {unbordered_table_count} saved to {excel_filename}.")
    else:
        print(f"Table {i+1} is bordered or doesn't match criteria.")

# Check if any unbordered tables were found
if unbordered_table_count == 0:
    print("No unbordered tables found.")


