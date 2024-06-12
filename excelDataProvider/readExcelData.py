import openpyxl

class ReadExcelData:
    def __init__(self, excel_file):
        self.excel_file = excel_file

    def read_data(self, sheet_name):
        workbook = openpyxl.load_workbook(self.excel_file)
        sheet = workbook[sheet_name]

        data = []
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(row)

        return data