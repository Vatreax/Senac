import sqlite3

conect = sqlite3.connect('bancoDados.db')

cursor = conect.cursor()

cursor.execute('''
        CREATE TABLE usuario(
            id integer primary key autoincrement,
            nome text not null,
            email text not null
        )   
''')
   
conect.commit()
conect.close()