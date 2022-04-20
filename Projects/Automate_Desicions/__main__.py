import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS tshirts 
            (sku text PRIMARY KEY, name text, size text, price real)''')

cur.execute('''INSERT OR IGNORE INTO tshirts VALUES
                ('SKU1235', 'Black Logo Tshirt', 'medium', '24.0')''')

con.commit()