import sqlite3


class Database:
    def __init__(self, db): #instruktor; sve metode u klasi uzimaju self i preno u db
        self.conn = sqlite3.connect(db) #konekcija sa db
        self.cur = self.conn.cursor() #cursor izvrsava naredbe
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS tel (id INTEGER PRIMARY KEY, marka text, model text, godiste text, cijena text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM tel")
        rows = self.cur.fetchall()
        return rows

    def insert(self, marka, model, godiste, cijena):
        self.cur.execute("INSERT INTO tel VALUES (NULL, ?, ?, ?, ?)",
                         (marka, model, godiste, cijena))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM tel WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, marka, model, godiste, cijena):
        self.cur.execute("UPDATE tel SET marka = ?, model = ?, godiste = ?, cijena = ? WHERE id = ?",
                         (marka, model, godiste, cijena, id))
        self.conn.commit()

    def __del__(self): #destruktor
        self.conn.close() #zatvaranje konekcije
