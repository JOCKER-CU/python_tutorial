# import camelot

# # Path to the PDF file
# pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"

# # Extract tables from the PDF
# tables = camelot.read_pdf(pdf_path, pages="all", flavor="lattice")  # Use 'stream' for borderless tables

# # Print the number of tables found
# print(f"Total tables extracted: {tables.n}")

# # Save each table to a CSV file
# for i, table in enumerate(tables):
#     table.to_csv(f"table_{i + 1}.csv")  # Save as CSV
#     print(f"Table {i + 1} saved as table_{i + 1}.csv")

# # Alternatively, save all tables to a single Excel file
# tables.export("all_tables.xlsx", f="excel")  # Save as Excel
# print("All tables saved as all_tables.xlsx")


import camelot

# Path to the PDF file
pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"

# Extract tables from the PDF
tables = camelot.read_pdf(pdf_path, pages="all", flavor="lattice")  # Use 'stream' for borderless tables

# Print the number of tables found
print(f"Total tables extracted: {tables.n}")

# Save each table to an HTML file
for i, table in enumerate(tables):
    html_path = f"table_{i + 1}.html"  # Define the HTML file path
    table.to_html(html_path)  # Save as HTML
    print(f"Table {i + 1} saved as {html_path}")

# Alternatively, save all tables to a single HTML file
with open("all_tables.html", "w", encoding="utf-8") as file:
    for i, table in enumerate(tables):
        file.write(f"<h2>Table {i + 1}</h2>\n")  # Add a header for each table
        file.write(table.df.to_html())  # Convert the table to HTML and write to file
        file.write("\n\n")  # Add spacing between tables
print("All tables saved as all_tables.html")