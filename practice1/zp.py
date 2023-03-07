import requests
import os
import shutil
import zipfile
import xlrd3 as xlrd

toDir = 'c://temp//tmp'

if os.path.exists(toDir):
    shutil.rmtree(toDir)
os.mkdir(toDir)

url = 'https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip'
r = requests.get(url)
with open('c://temp/tmp.zip', 'wb') as f:
    f.write(r.content)
    with zipfile.ZipFile(f.name, 'r') as zf:
        zf.extractall(toDir)
'
sp = []
for i in os.listdir(toDir):
    wb = xlrd.open_workbook(toDir+'//'+i)
    sh = wb.sheet_by_index(0)
    sp.append((sh.cell_value(1, 1), int(sh.cell_value(1, 3))))
sp = sorted(sp)
with open('c://temp/out.txt', 'w', encoding='utf-8') as f:
    for i in range(1000):
#    print(*sp[i])
        f.write(sp[i][0]+" "+str(sp[i][1])+"\n")
