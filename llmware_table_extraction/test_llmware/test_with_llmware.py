# from llmware.parsers import Parser
# import json

# # Function to convert a table to HTML
# def table_to_html(table):
#     html = "<table border='1'>\n"
#     for row in table:
#         html += "  <tr>\n"
#         for cell in row:
#             html += f"    <td>{cell}</td>\n"
#         html += "  </tr>\n"
#     html += "</table>"
#     return html
# # Example usage  C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf, C:\Users\hanna\Downloads\Insurance Claim Form 1.pdf
# # Path to your PDF file
# pdf_path = r"your_file.pdf"

# # Initialize the parser
# parser = Parser()

# # Parse the PDF and extract tables
# tables = parser.parse_pdf(pdf_path, extract_tables=True)

# # Save tables as JSON
# json_output = {"tables": tables}
# with open("extracted_tables.json", "w") as json_file:
#     json.dump(json_output, json_file, indent=4)
# print("Tables saved to 'extracted_tables.json'")

# # Save tables as HTML
# html_output = "<html><body>\n"
# for i, table in enumerate(tables):
#     html_output += f"<h2>Table {i+1}</h2>\n"
#     html_output += table_to_html(table)
# html_output += "</body></html>"

# with open("extracted_tables.html", "w") as html_file:
#     html_file.write(html_output)
# print("Tables saved to 'extracted_tables.html'")



# from llmware.parsers import Parser
# import json

# # Function to convert a table to HTML
# def table_to_html(table):
#     html = "<table border='1'>\n"
#     for row in table:
#         html += "  <tr>\n"
#         for cell in row:
#             html += f"    <td>{cell}</td>\n"
#         html += "  </tr>\n"
#     html += "</table>"
#     return html


# # # Example usage  C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf, C:\Users\hanna\Downloads\Insurance Claim Form 1.pdf

# # Path to your PDF file
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # Initialize the parser
# parser = Parser()

# # Parse the PDF
# parsed_data = parser.parse(pdf_path)

# # Extract tables from the parsed data
# tables = []
# for page in parsed_data:
#     if "tables" in page:
#         tables.extend(page["tables"])

# # Save tables as JSON
# json_output = {"tables": tables}
# with open("extracted_tables.json", "w") as json_file:
#     json.dump(json_output, json_file, indent=4)
# print("Tables saved to 'extracted_tables.json'")

# # Save tables as HTML
# html_output = "<html><body>\n"
# for i, table in enumerate(tables):
#     html_output += f"<h2>Table {i+1}</h2>\n"
#     html_output += table_to_html(table)
# html_output += "</body></html>"

# with open("extracted_tables.html", "w") as html_file:
#     html_file.write(html_output)
# print("Tables saved to 'extracted_tables.html'")


# from llmware.parsers import TableParser
# import json

# # Function to convert a table to HTML
# def table_to_html(table):
#     html = "<table border='1'>\n"
#     for row in table:
#         html += "  <tr>\n"
#         for cell in row:
#             html += f"    <td>{cell}</td>\n"
#         html += "  </tr>\n"
#     html += "</table>"
#     return html

# # Path to your PDF file
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # Initialize the TableParser
# table_parser = TableParser()

# # Parse the PDF and extract tables
# tables = table_parser.parse(pdf_path)

# # Save tables as JSON
# json_output = {"tables": tables}
# with open("extracted_tables.json", "w") as json_file:
#     json.dump(json_output, json_file, indent=4)
# print("Tables saved to 'extracted_tables.json'")

# # Save tables as HTML
# html_output = "<html><body>\n"
# for i, table in enumerate(tables):
#     html_output += f"<h2>Table {i+1}</h2>\n"
#     html_output += table_to_html(table)
# html_output += "</body></html>"

# with open("extracted_tables.html", "w") as html_file:
#     html_file.write(html_output)
# print("Tables saved to 'extracted_tables.html'")




from llmware.parsers import Parser
import json

# Function to convert a table to HTML
def table_to_html(table):
    html = "<table border='1'>\n"
    for row in table:
        html += "  <tr>\n"
        for cell in row:
            html += f"    <td>{cell}</td>\n"
        html += "  </tr>\n"
    html += "</table>"
    return html

# Path to your PDF file
pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# Initialize the Parser
parser = Parser()

# Parse the PDF
parsed_data = parser.parse(pdf_path)

# Extract tables from the parsed data
tables = []
for page in parsed_data:
    if "tables" in page:
        tables.extend(page["tables"])

# Save tables as JSON
json_output = {"tables": tables}
with open("extracted_tables.json", "w") as json_file:
    json.dump(json_output, json_file, indent=4)
print("Tables saved to 'extracted_tables.json'")

# Save tables as HTML
html_output = "<html><body>\n"
for i, table in enumerate(tables):
    html_output += f"<h2>Table {i+1}</h2>\n"
    html_output += table_to_html(table)
html_output += "</body></html>"

with open("extracted_tables.html", "w") as html_file:
    html_file.write(html_output)
print("Tables saved to 'extracted_tables.html'")