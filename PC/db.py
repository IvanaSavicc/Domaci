import sqlite3


class Database:
    def __init__(self, db): #instruktor; sve metode u klasi uzimaju self i preno u db
        self.conn = sqlite3.connect(db) #konekcija sa db
        self.cur = self.conn.cursor() #cursor izvrsava naredbe
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS  pc (id INTEGER PRIMARY KEY, proizvodjac text, model text, spec text, cijena text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM  pc")
        rows = self.cur.fetchall()
        return rows

    def insert(self, proizvodjac, model, spec, cijena):
        self.cur.execute("INSERT INTO pc VALUES (NULL, ?, ?, ?, ?)",
                         (proizvodjac, model, spec, cijena))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM pc WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, proizvodjac, model, spec, cijena):
        self.cur.execute("UPDATE  pc SET marka = ?, model = ?, godiste = ?, cijena = ? WHERE id = ?",
                         (proizvodjac, model, spec, cijena, id))
        self.conn.commit()

    def __del__(self): #destruktor
        self.conn.close() #zatvaranje konekcije
