import xlrd3 as xlrd

wb = xlrd.open_workbook('trekking3.xlsx')
sh = wb.sheet_by_name('Справочник')
sp = {sh.cell_value(i, 0): (sh.cell_value(i, 1) or 0, sh.cell_value(i, 2) or 0, sh.cell_value(i, 3) or 0, sh.cell_value(i, 4) or 0) for i in range(1, sh.nrows)}

sh = wb.sheet_by_name('Раскладка')
it = {}
for i in range(1, sh.nrows):
    if sh.cell_value(i, 1) in sp:
        den = int(sh.cell_value(i, 0))
        if den not in it:
            it[den] = [0, 0, 0, 0]
        for j in range(4):
            it[den][j] += sp.get(sh.cell_value(i, 1))[j] / 100 * sh.cell_value(i, 2)
for i in it.values():
    vr = [int(el) for el in i]
    print(*vr)
