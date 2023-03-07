import xlrd3 as xlrd

wb = xlrd.open_workbook('trekking2.xlsx')
sh = wb.sheet_by_name('Справочник')
sp = {sh.cell_value(i, 0): (sh.cell_value(i, 1) or 0, sh.cell_value(i, 2) or 0, sh.cell_value(i, 3) or 0, sh.cell_value(i, 4) or 0) for i in range(1, sh.nrows)}

sh = wb.sheet_by_name('Раскладка')
it = [0,0,0,0]
for i in range(1, sh.nrows):
    if sh.cell_value(i, 0) in sp:
        for j in range(4):
            it[j] += sp.get(sh.cell_value(i, 0))[j] / 100 * sh.cell_value(i, 1)
for i in it:
    print(int(i), end=' ')