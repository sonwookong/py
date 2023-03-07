import requests
import re

s = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').text
reg = '<code>(.*?)</code>'
sp = re.findall(reg, s)
col = {i: sp.count(i) for i in sp}
m = max(col.values())
sp = sorted([i for i in col if col[i] == m])
print(*sp, sep=' ')
