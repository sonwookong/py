import xlrd3 as xlrd

wb = xlrd.open_workbook('salaries.xlsx')
sh = wb.sheet_by_index(0)
r, c = sh.nrows, sh.ncols
el = (c - 1)//2
sp_s = {sh.cell_value(i, 0) : sorted(sh.row_values(i, 1))[el] for i in range(1, r)}
print(max(sp_s, key=sp_s.get), end=' ')

sp_s = {sh.cell_value(0, i) : sum(sh.col_values(i, 1))/(r-1) for i in range(1, c)}
#print(sp_s)
print(max(sp_s, key=sp_s.get))