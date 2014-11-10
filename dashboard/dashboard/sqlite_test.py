import sqlite3

conn = sqlite3.connect('mimic2.db')
c = conn.cursor()

for row in c.execute('SELECT * FROM d_patients LIMIT 10'):
        print row

conn.close()
