# import camelot

# # Path to the PDF file
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # Extract tables from specific pages using the lattice flavor
# tables = camelot.read_pdf(
#     pdf_path,
#     pages='1,2',  # Extract tables from pages 1 and 2
#     flavor='lattice',  # Use lattice flavor
#     table_areas=['50,500,400,100'],  # Define a specific area to extract tables from
#     strip_text='\n'  # Strip newlines from text
# )

# print(f"Number of tables extracted: {len(tables)}")

# # Iterate through the extracted tables
# for i, table in enumerate(tables):
#     print(f"Table {i+1}:\n{table.df}\n")
#     print("=====================================\n")
    
#     # Save table as CSV
#     table.to_csv(f"table_{i+1}.csv")

import camelot

# Set the Ghostscript path explicitly
camelot.set_ghostscript_path(r"C:\Program Files\gs\gs10.04.0\bin\gswin64c.exe")

# Path to the PDF file
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# Extract tables from the PDF
tables = camelot.read_pdf(pdf_path, pages='all')  # 'all' to extract tables from all pages

print(f"Number of tables extracted: {len(tables)}")

# Iterate through the extracted tables
for i, table in enumerate(tables):
    print(f"Table {i+1}:\n{table.df}\n")
    print("=====================================\n")
    
    # Save table as CSV
    table.to_csv(f"table_{i+1}.csv")