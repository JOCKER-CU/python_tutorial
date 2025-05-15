# import pdfplumber

# # Open the PDF
# with pdfplumber.open(r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf") as pdf:
#     for page_number, page in enumerate(pdf.pages, start=1):
#         # Extract tables
#         tables = page.extract_tables()
#         for i, table in enumerate(tables):
#             print(f"Page {page_number} Table {i+1}:")
#             for row in table:
#                 print(row)
#             print("\n")


# import pdfplumber
# import pandas as pd

# # Paths for input PDF and output Excel
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"
# excel_path = "output.xlsx"  # Specify your desired output path

# # Process the PDF and write tables to Excel
# with pdfplumber.open(pdf_path) as pdf, pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
#     for page_number, page in enumerate(pdf.pages, start=1):
#         # Extract tables from the current page
#         tables = page.extract_tables()
        
#         for table_number, table in enumerate(tables, start=1):
#             if table:  # Proceed only if the table is not empty
#                 # Convert the table to a DataFrame
#                 df = pd.DataFrame(table)
#                 print('Table data frame: ', df)
                
#                 # Generate sheet name (Excel limits sheet names to 31 characters)
#                 sheet_name = f"Page {page_number} T{table_number}"
#                 sheet_name = sheet_name[:31]  # Truncate if too long
                
#                 # Write the DataFrame to Excel
#                 df.to_excel(
#                     writer,
#                     sheet_name=sheet_name,
#                     index=False,    # Do not include row indices
#                     header=False    # Do not add DataFrame column headers
#                 )


# extract table and text data from the pdf

import pdfplumber
import json
 
# Path to the input PDF  "C:\Users\hanna\Downloads\New-Motor-Insurance-Brochure-MM.pdf" "C:\Users\hanna\Downloads\postgresql-15-US.pdf" 
# "C:\\Users\\hanna\\Downloads\\DLMM_APPLICATION_FORM_LIFE_PRO-Dai-ichi_Life_Pro_Application_Form-29cf229ce3964d16b75bada4f4ab5d27 1.pdf"
pdf_path = r"C:\Users\hanna\Downloads\DLMM_ACR_FORM-Agent_Confidential_Report_Form-5740f24894744cf9 1.pdf"

# List to store the extracted data
extracted_data = []

# Open the PDF and process each page
with pdfplumber.open(pdf_path) as pdf:
    for page_number, page in enumerate(pdf.pages, start=1):
          # Extract tables from the page
        tables = page.extract_tables()
        for table_number, table in enumerate(tables, start=1):
            if table:  # If the table is not empty
                extracted_data.append({
                    "data_type": "table",
                    "page_id": page_number,
                    "data": table
                })
                print("================================================")
                print("this is table data:" , table)
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
            print("this is text data:" + text)
            print("================================================")
      
# Save the extracted data as a JSON file
output_json_path = "DLMM_ACR_FORM-Agent_Confidential_Report_Form_add_split_method.json"
with open(output_json_path, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"Data extracted and saved to {output_json_path}")



# import pdfplumber
# import json

# # Path to the input PDF
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # List to store the extracted data
# extracted_data = []

# # Open the PDF and process each page
# with pdfplumber.open(pdf_path) as pdf:
#     for page_number, page in enumerate(pdf.pages, start=1):
#         # Extract tables from the page
#         tables = page.extract_tables()
#         table_texts = set()  # To store text from tables and avoid duplication

#         for table_number, table in enumerate(tables, start=1):
#             if table:  # If the table is not empty
#                 # Flatten the table and add its text to the set
#                 for row in table:
#                     for cell in row:
#                         if cell:  # If the cell is not empty
#                             table_texts.add(cell.strip())

#                 # Add the table data to the extracted_data list
#                 extracted_data.append({
#                     "data_type": "table",
#                     "page_id": page_number,
#                     "data": table
#                 })
#                 print("================================================")
#                 print(f"Page {page_number} - Table {table_number} Data:\n{table}")
#                 print("================================================")

#         # Extract text from the page
#         text = page.extract_text()
#         if text:  # If text is found
#             # Filter out text that is already part of the tables
#             filtered_text = []
#             for line in text.splitlines():
#                 line = line.strip()
#                 if line and line not in table_texts:  # Exclude table text
#                     filtered_text.append(line)

#             # Join the filtered text back into a single string
#             filtered_text = "\n".join(filtered_text)

#             if filtered_text:  # If there is any non-table text
#                 extracted_data.append({
#                     "data_type": "text",
#                     "page_id": page_number,
#                     "data": filtered_text
#                 })
#                 print("================================================")
#                 print(f"Page {page_number} - Text Data:\n{filtered_text}")
#                 print("================================================")

# # Save the extracted data as a JSON file
# output_json_path = "output3.json"
# with open(output_json_path, "w", encoding="utf-8") as json_file:
#     json.dump(extracted_data, json_file, indent=4)

# print(f"Data extracted and saved to {output_json_path}")





# import pdfplumber
# import json

# # Path to the input PDF
# pdf_path = r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf"

# # Dictionary to store the extracted data
# extracted_data = {}

# # Open the PDF and process each page
# with pdfplumber.open(pdf_path) as pdf:
#     for page_number, page in enumerate(pdf.pages, start=1):
#         # Initialize the page entry in the dictionary
#         extracted_data[page_number] = {
#             "text": None,  # Placeholder for text data
#             "tables": []   # Placeholder for table data
#         }

#         # Extract text from the page
#         text = page.extract_text()
#         if text:  # If text is found
#             extracted_data[page_number]["text"] = text
#             print(f"Page {page_number} - Text Data:\n{text}\n")

#         # Extract tables from the page
#         tables = page.extract_tables()
#         for table_number, table in enumerate(tables, start=1):
#             if table:  # If the table is not empty
#                 extracted_data[page_number]["tables"].append(table)
#                 print(f"Page {page_number} - Table {table_number} Data:\n{table}\n")

# # Save the extracted data as a JSON file
# output_json_path = "output2.json"
# with open(output_json_path, "w", encoding="utf-8") as json_file:
#     json.dump(extracted_data, json_file, indent=4)

# print(f"Data extracted and saved to {output_json_path}")