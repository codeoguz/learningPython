from xmlrpc.client import ResponseError
from bs4 import BeautifulSoup
import requests
import sqlite3

dbname = 'ebursay'

con = sqlite3.connect(f'././{dbname}.db')

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

pages = [
    'https://e.bursay.com.tr/isitma',
    'https://e.bursay.com.tr/kazan',
    'https://e.bursay.com.tr/sogutma',
    'https://e.bursay.com.tr/fan',
    'https://e.bursay.com.tr/dogalgaz-tesisat-malzemesi',
    'https://e.bursay.com.tr/pompa',
    'https://e.bursay.com.tr/sihhi-tesisat-malzemesi',
    'https://e.bursay.com.tr/tesisat-malzemesi',
    'https://e.bursay.com.tr/Vana',
    'https://e.bursay.com.tr/hirdavat'
]

for page in pages:
    i = 0
    while True:             
        i += 1
        starturl = f'{page}/page/{i}'  
        
        r = requests.get(starturl)
        sp =  BeautifulSoup(r.text, 'html.parser')
        
        if not r.ok:
            break   
        
        recipe_list = parse_soup(sp)

        print(f'''
              Link: {page}
              Index: {i}
              Length: {len(recipe_list)}
              ''')
        
        cur.executemany("INSERT OR IGNORE INTO products VALUES (?,?,?)", recipe_list)
        con.commit()
        
