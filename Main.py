import requests
from bs4 import BeautifulSoup
import json


def makeRequest():
    # Requests.post requiere la url y los datos a enviar.
    url = "https://postnl.post/details/"
    myData = {'barcodes': 'RU866553307NL\nRU806590792NL'}
    re = requests.post(url, data = myData)
    return re

soup = BeautifulSoup(makeRequest().content, 'html.parser')
with open('response.html', 'w', encoding = "utf-8") as f:
    f.write(soup.prettify())

mainData = soup.find(id = "datatables")
shipments = mainData.find_all(class_="subitems closed odd")

status = {}
for item in shipments:
    trackID = item.find(class_="barcode").get_text().strip()
    date = item.find(class_="date").get_text().strip().split(' ')[0]
    status = item.find(class_="status").get_text().strip()
    output[trackID] = {'date': date, 'status': status}

