import requests
import xmltodict

url = 'https://stepik.org/media/attachments/lesson/245681/map2.osm'
r = requests.get(url)
xml = r.text
px = xmltodict.parse(xml)

kol = 0

for node in px['osm']['node']:
    if 'tag' in node:
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == 'amenity' and tag['@v'] == 'fuel':
                    kol += 1
                elif isinstance(tags, dict):
                    if tags['@k'] == 'amenity' and tags['@v'] == 'fuel':
                        kol += 1

print(kol)