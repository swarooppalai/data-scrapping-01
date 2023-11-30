# Importing libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import csv
import pandas as pd

# Include this library if you want to add automated mailing when there is a price drop or certain conditions are satisfied
import smtplib   

# Connect to the website
url='https://www.flipkart.com/fujifilm-x-series-x-t4-mirrorless-camera-body-only/p/itm6665b78dd1a1c?pid=DLLFSY4X95PUZVQD&lid=LSTDLLFSY4X95PUZVQDDWQQRK&marketplace=FLIPKART&store=jek%2Fp31%2Ftrv&srno=b_1_1&otracker=browse&fm=organic&iid=en_MTHgp4TAJJai4ge6sQJohSkW28eIkXa5yaPTBufaoU5fzaGxvwJE_zNcsjylrQaJDyWUNmiSAbyDlhGo1sAlFg%3D%3D&ppt=hp&ppn=homepage&ssid=k5pcd4bxhlqybsow1701245161642'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15", 
    "X-Amzn-Trace-Id": "Root=1-65664fe0-10060fcb7af6b91f0ec7c1f4"}

# Fetch the web page
page = requests.get(url, headers=headers)
soup1 = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

# Extract product details
title = soup2.find('span', class_='B_NuCI').get_text()
price = soup2.find('div', class_="_30jeq3 _16Jk6d").get_text()
rating = soup2.find('div', class_="_3LWZlK").get_text()

# Clean and format data
title = title.strip()
price = price.replace(',', '')
price = price.strip()[1:]
rating = rating.strip()
now = datetime.date.today()

# Create an Excel sheet
headers = ['Product Name', 'Price', 'Ratings', 'import time']
data = [title, price, rating, now]

# Write data to CSV file
with open('flipkart_data_scrapping.csv', 'w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(data)

# Append data to the CSV file
with open('flipkart_data_scrapping.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(r'/location/flipkart_data_scrapping.csv')    
print(df)  

# Function to check price automatically
def check_price(headers):
    page = requests.get(url, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find('span', class_='B_NuCI').get_text()
    price = soup2.find('div', class_="_30jeq3 _16Jk6d").get_text()
    rating = soup2.find('div', class_="_3LWZlK").get_text()

    title = title.strip()
    price = price.replace(',', '')
    price = price.strip()[1:]
    rating = rating.strip()

    today = datetime.date.today()

    headers = ['Product Name', 'Price', 'Ratings', 'import time']
    data = [title, price, rating, today]

    # Append data to the CSV file
    with open('flipkart_data_scrapping.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

# Introducing automation to check price automatically
while True:
    check_price(headers)
    time.sleep(3600)
    pass

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(r'/location/flipkart_data_scrapping.csv')    
print(df)
