import requests
from bs4 import BeautifulSoup
import json
import csv

''' Given a CSV file with Order Names and Tracking IDs, will make a POST request
    to post.nl with each tracking ID **separately** and parse the answer content, 
    retrieving from the last status update: Datetime and status message. 
'''

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
    mainContent = soup.find(id="datatables").find(class_="first detail").find_all("td")
    ans['Datetime'] = mainContent[0].get_text().strip()
    ans['Status'] = mainContent[1].get_text().strip()
    return ans

def getOrders(csv_file):
    with open(csv_file, 'r') as f:
        csv_reader = csv.reader(f, delimiter = ";")
        rowCount = 0
        orders = []
        # Store Order Name, Tracking ID
        for row in csv_reader:
            if rowCount > 0:
                orders.append({
                    'Name': row[0],
                    'TrackingID': row[1]
                })
            rowCount += 1
    return orders

def main():
    url = "https://postnl.post/details/"
    myOrders = getOrders('orders.csv')
    with open('Output.txt', 'w') as f:
        for order in myOrders:
            # The webpage requires tracking ID in this format
            request_data = {'barcodes': order['TrackingID']}
            # Parsing html data and getting the desired info
            orderInfo = parse(makeRequest(url, request_data))
            # Updating my orders
            order.update({'Status': orderInfo['Status'], 'Updated': orderInfo['Datetime']})
            message = f"{order['Name']}:\n\
                >>> {order['Status']}.\n\
                >>> Last Updated: {order['Updated']}\n"
            f.write(message)
            print(message)

main()
    

