from bs4 import BeautifulSoup
import requests
import sqlite3
import urllib

# create sqlite connection
conn = sqlite3.connect('topicimages.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS topicimages;')
c.execute('CREATE TABLE topicimages ( id integer primary key autoincrement, topic text not null, link text not null);')

def scrape_image(topic):
    # remove spaces from topic so URL doesn't eff itself
    topic = topic.replace(" ", "_")
    url = 'https://en.wikipedia.org/wiki/' + topic
    # get response
    wiki_response = requests.get(url)
    # soup conatins the html page
    soup = BeautifulSoup(wiki_response.text, 'html.parser')
    infobox_content = soup.find("table").find_all('img', src=True)
    img_link_raw = infobox_content[0]["src"].split("src=")[-1]
    # trim leading "//"
    img_link = img_link_raw[2:]
    print(img_link)
    return img_link
    c.execute('INSERT INTO topicimages (topic, img_link) VALUES (?,?)', [topic, img_link])

if __name__ == '__main__':
    scrape_image("Barack Obama")
    # proving to myself that this actually works
    cursor_object = c.execute('SELECT * from topicimages order by id desc')
    list = cursor_object.fetchall()
    print(list)
