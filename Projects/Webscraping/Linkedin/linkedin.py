from pydoc import getpager
from warnings import catch_warnings
from bs4 import BeautifulSoup
import requests
import sqlite3
import email
from html_table_extractor.extractor import Extractor

dbname = 'linkedin'

con = sqlite3.connect(f'{dbname}.db')
cur = con.cursor()



cur.execute('''CREATE TABLE IF NOT EXISTS recipes 
            (name text PRIMARY KEY, profession text, email text)''')

def getPage(url):
    r = requests.get(url)
    sp =  BeautifulSoup(r.text, 'html.parser')
    return sp

def parse_soup(sp):
    recipe_list = []
    page = sp.find_all('article', {'class': 'comments-comments-list__comment-item'})
    print(page)
    for recipe in page :
        try:
            name = recipe.find('span', {'class': 'comments-post-meta__name-text'}).text
            profession = recipe.find('span', {'class': 'comments-post-meta__headline'}).text
            email =  recipe.find('a', {'data-attribute-index': "0"}).text
        except:
            pass
        recipe_list.append((name, profession, email))
        
    return recipe_list




recipe_list = []


with open("linkedin.mhtml") as fp:
    message = email.message_from_file(fp)
    for part in message.walk():
        if (part.get_content_type() == "text/html"):
            soup = BeautifulSoup(part.get_payload(decode=False), 'html.parser')
            for table in soup.body.find_all("article", {'class': 'comments-comments-list__comment-item'}):
                print(table)
                extractor = Extractor(table)
                extractor.parse()
                print(extractor.return_list())
                try:
                    name = extractor.find('span', {'class': 'comments-post-meta__name-text'}).text
                    profession = extractor.find('span', {'class': 'comments-post-meta__headline'}).text
                    email =  extractor.find('a', {'data-attribute-index': "0"}).text

                    
                    
                    recipe_list.append((name, profession, email))
                except:
                    pass
                
                """ extractor = Extractor(table)
                extractor.parse()
                print(extractor.return_list())
                recipe_list = extractor.return_list() """

print(len(recipe_list))

try:
    cur.executemany("INSERT INTO recipes VALUES (?,?,?)", recipe_list)
    con.commit()
except: 
    pass 