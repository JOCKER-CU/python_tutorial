import camelot

# Path to the PDF file
pdf_path = r"C:\Users\hanna\Downloads\Insurance Claim Form 1.pdf"

# Extract tables from the PDF
tables = camelot.read_pdf(pdf_path, pages="all", flavor="lattice")  # Use 'stream' for borderless tables

# Print the number of tables found
print(f"Total tables extracted: {tables.n}")

# Save each table to a CSV file
for i, table in enumerate(tables):
    table.to_csv(f"table_{i + 1}.csv")  # Save as CSV
    print(f"Table {i + 1} saved as table_{i + 1}.csv")

# Alternatively, save all tables to a single Excel file
tables.export("all_tables.xlsx", f="excel")  # Save as Excel
print("All tables saved as all_tables.xlsx")