import  xlsxwriter  #it is a modual for use Excel

workbook = xlsxwriter.Workbook('demo3.xlsx')  #it is use create Excel File and file name is 'demo.xlsx'
worksheet = workbook.add_worksheet()   #it is use for create Sheet and add new sheet in Excel File
# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': True})
worksheet.set_column("A:A", 10)
worksheet.write('A1', 'Hello')# write data in sheet
worksheet.write('A2','world',bold)
worksheet.write(2,0,123,bold)        #write data in sheet
worksheet.write(3,0,123.456)
#worksheet.insert_image("B5", "logo.png")
  #close Excel file
workbook.close()