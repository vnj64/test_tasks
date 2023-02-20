import sqlite3


def init_db():
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS translations (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT, translit TEXT)')
    conn.commit()
    conn.close()
