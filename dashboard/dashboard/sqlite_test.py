# Running raw SQL query on a sqlite database 

import sqlite3

conn = sqlite3.connect('mimic2.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM d_meditems LIMIT 10'):
        print row

conn.close()
