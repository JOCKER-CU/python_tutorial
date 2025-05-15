import pdfplumber

pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"
output_file = "ExtractedTables.txt"

with pdfplumber.open(pdf_path) as pdf:
    with open(output_file, "w", encoding="utf-8") as file:
        for page_number, page in enumerate(pdf.pages, start=1):
            file.write(f"=== Page {page_number} ===\n")
            tables = page.extract_tables()
            if tables:
                for table in tables:
                    for row in table:
                        file.write("\t".join(row) + "\n")
                    file.write("\n")
            else:
                file.write("No tables found on this page.\n\n")
print(f"Table data has been extracted and saved to {output_file}")