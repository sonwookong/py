import requests
import xmltodict

url = 'https://stepik.org/media/attachments/lesson/245678/map1.osm'
r = requests.get(url)
xml = r.text
px = xmltodict.parse(xml)

im, nm = 0, 0

#print(px['osm']['node'])
for node in px['osm']['node']:
     if 'tag' in node:
         im += 1
     else:
         nm += 1
print(im, nm)
