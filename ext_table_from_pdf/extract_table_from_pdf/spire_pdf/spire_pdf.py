# from spire.pdf.common import *
# from spire.pdf import *

# # Create a PdfDocument object
# doc = PdfDocument()

# # Load the sample PDF file
# pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"
# doc.LoadFromFile(pdf_path)

# # Create a PdfTableExtractor object
# extractor = PdfTableExtractor(doc)

# # Create a list to store the extracted data
# extracted_data = []

# # Loop through the pages
# for page_index in range(doc.Pages.Count):
#     # Extract tables from the current page
#     table_list = extractor.ExtractTable(page_index)

#     if table_list is not None and len(table_list) > 0:
#         # Add a header to indicate the page number
#         extracted_data.append(f"=== Page {page_index + 1} ===\n")

#         # Loop through the tables in the list
#         for table in table_list:
#             # Get row and column counts
#             row_count = table.GetRowCount()
#             column_count = table.GetColumnCount()

#             # Loop through the rows and columns
#             for i in range(row_count):
#                 row_data = []
#                 for j in range(column_count):
#                     # Get text from the specific cell
#                     text = table.GetText(i, j)
#                     row_data.append(text)
                
#                 # Join row data with a delimiter (e.g., tab or comma)
#                 extracted_data.append("\t".join(row_data) + "\n")
            
#             # Add a separator between tables
#             extracted_data.append("\n")
#     else:
#         # If no tables are found on the page, add a message
#         extracted_data.append(f"=== Page {page_index + 1} ===\n")
#         extracted_data.append("No tables found on this page.\n\n")

# # Write the extracted data to a text file
# output_file = "Table.txt"
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write("".join(extracted_data))

# print(f"Table data has been extracted and saved to {output_file}")

# from spire.pdf.common import *
# from spire.pdf import *

# # Create a PdfDocument object
# doc = PdfDocument()

# # Load the sample PDF file
# pdf_path = r"C:\Users\hanna\Downloads\Documents\css.pdf"
# doc.LoadFromFile(pdf_path)

# # Create a list to store the extracted text
# extracted_text = []

# # Loop through the pages
# for page_index in range(doc.Pages.Count):
#     # Get the current page
#     page = doc.Pages[page_index]

#     # Extract text from the page
#     text = page.ExtractText()

#     # Add a header to indicate the page number
#     extracted_text.append(f"=== Page {page_index + 1} ===\n")
    
#     # Add the extracted text to the list
#     extracted_text.append(text + "\n\n")

# # Write the extracted text to a text file
# output_file = "ExtractedText.txt"
# with open(output_file, "w", encoding="utf-8") as file:
#     file.write("".join(extracted_text))

# print(f"Text has been extracted and saved to {output_file}")






