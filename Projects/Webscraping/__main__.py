from bs4 import BeautifulSoup
import requests
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS books 
            (title text PRIMARY KEY, price real, stock text)''')

def clean(item):
    return item.strip().replace('Â', '').replace('£', '')

def getPage(url):
    r = requests.get(url)
    sp =  BeautifulSoup(r.text, 'html.parser')
    return sp

def parse_soup(sp):
    book_list = []
    article = sp.find_all('article', {'class': 'product_pod'})
    for books in article:
        title = books.find('img', {'class':'thumbnail'})['alt']
        price = float(clean(books.find('p', {'class': 'price_color'}).text))
        stock = clean(books.find('p', {'class': 'instock availability'}).text)
        book_list.append((title, price, stock))
    return book_list

for i in range(49):
    i = i + 1
    starturl = f'https://books.toscrape.com/catalogue/page-{i}.html'
    
    sp = getPage(starturl)
    book_list = parse_soup(sp)

    cur.executemany("INSERT OR IGNORE INTO books VALUES (?,?,?)", book_list)
    con.commit()