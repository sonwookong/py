# to open/create a new html file in the write mode
f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
ht = """<html>
<body>
<table>
"""
for i in range(1,11):
    ht += "<tr>\n"
    for j in range(1,11):
        ht += "<td>"+str(i*j)+"</td>\n"
        j += 1
    ht += "</tr>\n"
    i += 1
ht += """</table>
</body>
</html>
"""

# writing the code into the file
f.write(ht)

# close the file
f.close()
