from bs4 import BeautifulSoup
import requests
import sqlite3

# create sqlite connection
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS neighborhoods;')
c.execute('CREATE TABLE neighborhoods ( id integer primary key autoincrement, name text not null);')

# get response
neighborhood_response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

# soup conatins the html page
soup = BeautifulSoup(neighborhood_response.text, 'html.parser')

# create table of neighborhoods by grabbing the table and all rows in that table
city_info_table = soup.table
table_rows = city_info_table("tr")
# iterate over all rows, grab the second to last row
for row in table_rows:
    neighborhood = row.contents[-2].text
    # strip commas and remove spaces and store each neighborhood
    stripped_neighborhoods = [x.strip() for x in neighborhood.split(',')]
    for n in stripped_neighborhoods:
        c.execute('INSERT INTO neighborhoods (name) VALUES (?)', [n])
        print(n)

# proving to myself that this works
cursor_object = c.execute('SELECT * from neighborhoods order by id desc')
list = cursor_object.fetchall()
print(list)
