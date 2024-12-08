
import sqlite3


class Connect():
    def __init__(self, name:str) -> None:
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
        self.cursor.executescript('''
            CREATE TABLE IF NOT EXISTS Sales (
                   id INTEGER PRIMARY KEY,
                   title TEXT NOT NULL,
                   price REAL NOT NULL,
                   date DATE
            )
        ''')
        self.connection.commit()

    def insert(self, title:str, price:float, date:str) -> None:
        self.cursor = self.connection.cursor()
        self.cursor.execute('INSERT INTO Sales (title, price, date) VALUES (?, ?, ?)', (title, price, date))
        self.connection.commit()
    
    def __del__(self):
        self.connection.close()