
import requests as req
from bs4 import BeautifulSoup

resp = req.get('https://stepik.org/media/attachments/lesson/209723/5.html')  # скачиваем файл
soup = BeautifulSoup(resp.text, 'html.parser')  # делаем суп

sp = [int(i.text) for i in soup.find_all('td')]
print(sum(sp))