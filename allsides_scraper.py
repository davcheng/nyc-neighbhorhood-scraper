from bs4 import BeautifulSoup
import requests
import sqlite3

# create sqlite connection
conn = sqlite3.connect('newssource.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS newssource;')
c.execute('CREATE TABLE newssource ( id integer primary key autoincrement, name text not null, bias_score number);')

# converts string to bias score
def bias_converter(bias_text):
    bias_score = 0
    if bias_text == "Bias: Right":
        bias_score = 1
    if bias_text == "Bias: Lean Right":
        bias_score = .5
    if bias_text == "Bias: Center":
        bias_score = 0
    if bias_text == "Bias: Lean Left":
        bias_score = -.5
    if bias_text == "Bias: Left":
        bias_score = -1
    return bias_score


def scrape_allsides():
    # get response
    neighborhood_response = requests.get('http://www.allsides.com/bias/bias-ratings')

    # soup conatins the html page
    soup = BeautifulSoup(neighborhood_response.text, 'html.parser')

    # create table of neighborhoods by grabbing the table and all rows in that table
    bias_table = soup.table
    table_rows = bias_table("tr")
    # grab img alt tags
    bias_list = [img["alt"] for img in bias_table.select("img[alt]")]

    # ghetto loop count used for indexing the bias list to the list of sources
    loop_count=-1
    for row in table_rows:
        # iterate over all rows, grab the first row
        source_name_list = row.contents[1].text
        # this finds all whatever tags
        # rating = row.contents[3].find(lambda tag: tag.name=='img')
        # strip commas and remove spaces and store each neighborhood
        stripped_sources = [x.strip() for x in source_name_list.split(',')]
        for n in stripped_sources:
            if loop_count > 0:
                bias_score = bias_converter(bias_list[loop_count])
                c.execute('INSERT INTO newssource (name, bias_score) VALUES (?, ?)', [n, bias_score])
        loop_count+=1




if __name__ == '__main__':
    scrape_allsides()
    # proving to myself that this actually works
    cursor_object = c.execute('SELECT * from newssource order by id desc')
    list = cursor_object.fetchall()
    print(list)
