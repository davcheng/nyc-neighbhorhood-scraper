from bs4 import BeautifulSoup
import requests
import sqlite3

# create sqlite connection
conn = sqlite3.connect('country.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS country;')
c.execute('CREATE TABLE country ( id integer primary key autoincrement, country_name text not null, country_population integer);')

def get_country_pop(country_name):

    response = requests.get('https://en.wikipedia.org/wiki/',country_name)
    soup = BeautifulSoup(response.text, 'html.parser')
    yo = 1
    print(response)
    # return(1232)

def scrape_countries():
    # get response
    country_response = requests.get('https://en.wikipedia.org/wiki/List_of_sovereign_states#List_of_states')
    # soup conatins the html page
    soup = BeautifulSoup(country_response.text, 'html.parser')
    # create table of neighborhoods by grabbing the table and all rows in that table
    country_info_table = soup.table
    table_rows = country_info_table("tr")

    # grab country names
    for row in table_rows:
        country_name = row.contents[1]
        a_tag = country_name.a
        if a_tag:
            country_name = a_tag.contents[0]
            country_population = get_country_pop(country_name)
            # store into db
            c.execute('INSERT INTO neighborhood (country_name, country_population) VALUES (?)', [country_name , country_population])
            print(get_country_pop(country_name))


    # # strip commas and remove spaces and store each neighborhood
    # stripped_neighborhoods = [x.strip() for x in neighborhood.split(',')]
    # for n in stripped_neighborhoods:
    #     c.execute('INSERT INTO neighborhoods (name) VALUES (?)', [n])
    #     print(n)

# # proving to myself that this works
# cursor_object = c.execute('SELECT * from neighborhoods order by id desc')
# list = cursor_object.fetchall()
# print(list)


if __name__ == '__main__':
    scrape_countries()
