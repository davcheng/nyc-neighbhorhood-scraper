from bs4 import BeautifulSoup
import requests
import sqlite3

response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

print(response.text)

soup = BeautifulSoup(response, 'html.parser')

# print(soup.prettify())