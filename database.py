import sqlite3

def init_db():
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS credentials (
                      id INTEGER PRIMARY KEY,
                      site TEXT,
                      username TEXT,
                      password TEXT)''')
    conn.commit()
    conn.close()


def add_credential(site, username, password):
    conn = sqlite3.connect("vault.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO credentials (site, username, password) VALUES (?, ?, ?)",
                   (site, username, password))
    conn.commit()
    conn.close()
