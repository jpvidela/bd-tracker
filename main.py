import requests
from bs4 import BeautifulSoup
import json


def makeRequest(url, data):
# Makes requests and returns content
    # Requests.post requiere la url y los datos a enviar.
    re = requests.post(url, data = data)
    return re.content

def parse(content):
    # Parses html and returns desired data
    ans = {}
    soup = BeautifulSoup(content, 'html.parser')
    # Here's all the info I need
    mainContent = soup.find(id="datatables").find(class_="first_ detail").find_all("td")
    ans['Date'] = mainContent[0].get_text().strip().split(' ')[0]
    ans['Status'] = main[1].get_text().strip()
    return ans


url = "https://postnl.post/details/"
trackingIDs = ["RU866553307NL", "RU806590792NL"]

for id in trackingIDs:
    # The webpage requires tracking ID in this format
    request_data = {'barcodes': id}
    idStatus = parse(makeRequest(url, request_data))

