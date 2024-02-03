import xlsxwriter


# Create an new Excel file and add a worksheet.
workbook = xlsxwriter.Workbook("demo1.xlsx")
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column("A:B", 20)

# Add a bold format to use to highlight cells.
bold = workbook.add_format({"bold": True})
italic = workbook.add_format({"italic": True})
# Write some simple text.
worksheet.write("A1", "Hello")

# Text with formatting.
worksheet.write("A2", "World", bold)
worksheet.write("B2", "Rishabh", italic)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

#close Excel file
workbook.close()