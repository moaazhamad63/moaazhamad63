import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

products = [
    ('e-45612', 'moaaz', '.', '500'),
    ('e-78451', 'moas', 'game', '650'),
    ('c-12488', 'mfsad', 'game', '1200'),
    ('a-23571', 'vcf', 'game', '300'),
    ('c-74123', 'bonn', 'game', '759'),
    ('b-45632', 'bommm', 'game', '899'),
    ('e-21547', 'boring', 'game', '122'),
    ('b-74159', 'gssf', 'game', '456'),
]
# Query the database
cursor.executemany('INSERT INTO products VALUES(?,?,?,?)', products)
conn.commit()
conn.close()
