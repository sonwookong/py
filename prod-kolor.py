import xlrd3 as xlrd

wb = xlrd.open_workbook('trekking1.xlsx')
sh = wb.sheet_by_index(0)
sp = [(sh.cell_value(i, 0), sh.cell_value(i, 1)) for i in range(1, sh.nrows)]
sp = sorted(sp, key=lambda item: (-item[1], item[0]))
for i in sp:
    print(i[0], sep='\n')
