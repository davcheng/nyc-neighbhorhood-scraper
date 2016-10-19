from bs4 import BeautifulSoup
import requests
import sqlite3

# create sqlite connection
conn = sqlite3.connect('country.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS country;')
c.execute('CREATE TABLE country ( id integer primary key autoincrement, name text not null, population integer);')

# get response
country_response = requests.get('https://en.wikipedia.org/wiki/List_of_sovereign_states#List_of_states')

# soup conatins the html page
soup = BeautifulSoup(country_response.text, 'html.parser')

# create table of neighborhoods by grabbing the table and all rows in that table
country_info_table = soup.table
table_rows = country_info_table("tr")

print(table_rows)

# iterate over all rows, grab the second to last row
for row in table_rows:
    country_name = row.contents[1]
    print(country_name("a"))
    # # strip commas and remove spaces and store each neighborhood
    # stripped_neighborhoods = [x.strip() for x in neighborhood.split(',')]
    # for n in stripped_neighborhoods:
    #     c.execute('INSERT INTO neighborhoods (name) VALUES (?)', [n])
    #     print(n)

# # proving to myself that this works
# cursor_object = c.execute('SELECT * from neighborhoods order by id desc')
# list = cursor_object.fetchall()
# print(list)
