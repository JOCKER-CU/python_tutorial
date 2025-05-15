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