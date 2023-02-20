import sqlite3

from transliterate import translit


def transliterate(text):
    new = translit(text, 'ru', reversed=True)
    return new

def save_to_database(text, translit):
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute('INSERT INTO translations (text, translit) VALUES (?, ?)', (text, translit))
    conn.commit()
    conn.close()

def get_last_10_entries():
    conn = sqlite3.connect('db/database.db')
    c = conn.cursor()
    c.execute('SELECT text, translit FROM translations ORDER BY id DESC LIMIT 10')
    data = c.fetchall()
    conn.close()
    return data
