import camelot

# Extract tables
tables = camelot.read_pdf(r"C:\Users\hanna\Downloads\SALES-ILLUSTRATION-LIFEPRO.pdf", pages="all")

# Print tables as DataFrames
for i, table in enumerate(tables):
    print(f"Table {i+1}:\n{table.df}\n")
    print("=====================================\n")
    print(table)
    # Save table as CSV
    table.to_csv(f"table_{i+1}.csv")
