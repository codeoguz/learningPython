from ast import Try
from warnings import catch_warnings
from bs4 import BeautifulSoup
import requests
import sqlite3
dbname = 'ebursay.db'

con = sqlite3.connect(f'{dbname}.db')

cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS products 
            (name text PRIMARY KEY, photo text, price real)''')

def clean(item):
    return item.strip().replace('Â', '').replace('£', '')

def getPage(url):
    r = requests.get(url)
    sp =  BeautifulSoup(r.text, 'html.parser')
    return sp

def parse_soup(sp):
    recipe_list = []
    page = sp.find_all('li', {'class': 'jet-woo-builder-product'})

    for recipe in page :
        name =  recipe.find('div', {'class': 'jet-woo-builder-archive-product-title'}).text
        photo = recipe.find('img')['src']
        price = recipe.find('bdi').text
        recipe_list.append((name, photo, price))
        
        
    return recipe_list

for i in range(3):
    i = i + 1
    starturl = f'https://e.bursay.com.tr/fan/page/{i}'
    
    sp = getPage(starturl)
    recipe_list = parse_soup(sp)

    print(i, len(recipe_list))
    print(recipe_list)
    
    cur.executemany("INSERT OR IGNORE INTO products VALUES (?,?,?)", recipe_list)
    con.commit()
    
    
