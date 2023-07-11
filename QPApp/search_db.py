import sqlite3

conn = sqlite3.connect('pdf_links.db')


cursor = conn.cursor()


cursor.execute('SELECT * FROM PDF_LINKS')


rows = cursor.fetchall()


for row in rows:
    print(row)

cursor.close()
conn.close()
