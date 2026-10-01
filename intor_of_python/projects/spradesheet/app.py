import openpyxl as xl
from openpyxl.chart import BarChart , Reference

def process_workbook(filename) : 

    wb = xl.load_workbook('transactions.xlsx')
    sheet = wb.active

    for row in range(2, sheet.max_row + 1):
        cell = sheet.cell(row, 3)
        
        if cell.value is not None:
            correct_price = cell.value * 0.9
            sheet.cell(row, 4).value = correct_price

    values = Reference(
        sheet,
        min_row=2,
        max_row=sheet.max_row,
        min_col=4,
        max_col=4
    )      

    chart = BarChart()
    chart.add_data(values)
    sheet.add_chart(chart , 'e2')
    wb.save(filename)