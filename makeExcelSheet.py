from openpyxl import Workbook


def makeExcelSheet(rawData, file_name):
    wb = Workbook()
    ws = wb.active

    for i in rawData:
        ws.append(i)
    wb.save("extractedFile/"+file_name + '.xlsx')
