import pdfplumber
import json

# Path to the input PDF
pdf_path = r"C:\Users\hanna\Downloads\DLMM_APPLICATION_FORM_LIFE_PRO-Dai-ichi_Life_Pro_Application_Form-29cf229ce3964d16b75bada4f4ab5d27 1.pdf"

# List to store the extracted data
extracted_data = []

# Helper function to convert a table to Markdown format
def table_to_markdown(table):
    """
    Converts a table (list of lists) into a Markdown-formatted table.
    :param table: List of lists representing the table data.
    :return: A string containing the Markdown table.
    """
    if not table:
        return ""
    
    # Extract headers and rows
    headers = table[0]  # First row is the header
    rows = table[1:]    # Remaining rows are data
    
    # Create the Markdown table header
    markdown_table = "| " + " | ".join(headers) + " |\n"
    markdown_table += "| " + " | ".join(["---"] * len(headers)) + " |\n"
    
    # Add rows to the Markdown table
    for row in rows:
        markdown_table += "| " + " | ".join(row) + " |\n"
    
    return markdown_table

# Open the PDF and process each page
with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
        # Extract tables from the page
        tables = page.extract_tables()
        for table_number, table in enumerate(tables, start=1):
            if table:  # If the table is not empty
                # Convert the table to Markdown format
                markdown_table = table_to_markdown(table)
                
                # Append the Markdown table to the extracted data
                extracted_data.append({
                    "data_type": "table",
                    "page_id": page_number,
                    "data": markdown_table
                })
                print("================================================")
                print("This is table data (Markdown):\n", markdown_table)
                print("================================================")
        
        # Extract text from the page
        text = page.extract_text()
        if text:  # If text is found
            extracted_data.append({
                "data_type": "text",
                "page_id": page_number,
                "data": text.split("\n")
            })
            print("================================================")
            print("This is text data:\n", text)
            print("================================================")

# Save the extracted data as a JSON file
output_json_path = "markdown_DLMM_ACR_FORM-Agent_Confidential_Report_Form_add_split_method.json"
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"Extracted data saved to {output_json_path}")