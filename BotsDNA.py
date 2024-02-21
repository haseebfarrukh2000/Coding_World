import pandas as pd

# Read the Excel file
xl = pd.ExcelFile("extracted_data.xlsx")
initial_df = xl.parse("Sheet1")

# Get column names (excluding the first column)
column_names = initial_df.columns[1:]

# Create a new Excel writer
writer = pd.ExcelWriter("output.xlsx", engine="xlsxwriter")

# Iterate through column names and create sheets
for col_name in column_names:
    # Create a new DataFrame with "CustomerName" and the current column
    new_df = initial_df[["CustomerName", col_name]]

    # Write the data to a new sheet
    new_df.to_excel(writer, sheet_name=col_name, index=False)

# Save the Excel file
writer._save()
