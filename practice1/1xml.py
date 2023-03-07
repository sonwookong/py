import requests
import xmltodict
'''
url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
r = requests.get(url)
with open('map1.osm', 'wb') as f:
    f.write(r.content)
'''
fin = open('map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
print(parsedxml)
#print(parsedxml['osm']['node'][100]['@id'])