import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''


class Database:
    def __init__(self, nome):
        self.conn = sqlite3.connect(nome+".db")
        self.cursor = self.conn.cursor()
        self.note = self.cursor.execute('''CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);''')
    
    def add(self, note):
        self.cursor.execute('''INSERT INTO note (title, content) VALUES (?,?);''',(note.title, note.content))
        self.conn.commit()
    
    def get_all(self):
        lista = []
        cursor = self.conn.execute('SELECT id, title, content FROM note')
        for i in cursor:
            id_v = i[0]
            title_v = i[1]
            content_v = i[2]
            lista.append(Note(id=id_v, title=title_v, content=content_v))
        return lista

    def update(self, entry):
        self.cursor.execute('UPDATE note SET title = ? WHERE id = ?', (entry.title, entry.id))
        self.cursor.execute('UPDATE note SET content = ? WHERE id = ?', (entry.content, entry.id))
        self.conn.commit()
    
    def delete(self, note_id):
        self.cursor.execute('DELETE FROM note WHERE id = ?', (note_id,))
        self.conn.commit()


    
