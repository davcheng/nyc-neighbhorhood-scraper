from bs4 import BeautifulSoup
import requests
import sqlite3

# create sqlite connection
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS neighborhoods;''')
c.execute('''CREATE TABLE neighborhoods ( id integer primary key autoincrement, name text not null, CB text not null);''')

# get response
neighborhood_response = requests.get('https://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City')

soup = BeautifulSoup(neighborhood_response.text, 'html.parser')


text = title_tag.contents[-1]
for child in title_tag.children:
    print(child)

# c.execute("INSERT INTO neighborhoods (name) VALUES (?)", "yo")

# for row in c.execute('SELECT * FROM neighborhoods'):
#     print(row)

# t = ('RHAT',)
# c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(soup.prettify())
