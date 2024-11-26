import sqlite3

# ('''
#    create table usuario(
#                id integer primary key autoincrement,
#                nome text not null,
#                email text not null               
#    )
# ''')

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def conectar(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def executar(self, query, parametros):
        if parametros:
            self.cursor.execute(query,parametros)
        else:
            self.cursor.execute(query)
        self.conn.commit()
    
    def fet_do_all(self):
        return self.cursor.fetchall()
