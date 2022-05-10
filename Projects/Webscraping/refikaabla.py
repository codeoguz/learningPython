from warnings import catch_warnings
from bs4 import BeautifulSoup
import requests
import sqlite3

dbname = 'refikabla'

con = sqlite3.connect(f'{dbname}.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS recipes 
            (photo text PRIMARY KEY, category text, name text)''')

def getPage(url):
    r = requests.get(url)
    sp =  BeautifulSoup(r.text, 'html.parser')
    return sp

def parse_soup(sp):
    recipe_list = []
    page = sp.find_all('div', {'class': 'mutfak-yazisi-list-item'})
    for recipe in page :
        try:
            photo = recipe.find('img')['src']
            category = recipe.find('div', {'class': 'mutfak-yazisi-cat'}).text
            name =  recipe.find('div', {'class': 'mutfak-yazisi-title'}).text
        except:
            pass
        recipe_list.append((photo, category, name))
        
    return recipe_list

for i in range(35):
    i = i + 1
    starturl = f'https://www.refikaninmutfagi.com/tarifler/page/{i}/'
    
    sp = getPage(starturl)
    recipe_list = parse_soup(sp)

    print(i, len(recipe_list))
    
    try:
        cur.executemany("INSERT INTO recipes VALUES (?,?,?)", recipe_list)
        con.commit()
    except: 
        pass