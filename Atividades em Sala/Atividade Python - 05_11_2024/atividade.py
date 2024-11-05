import mysql.connector
from biblioteca import biblioteca
from usuario import usuario

class Database:
    def __init__(self, host, user, password, database):
        self.host = host 
        self.user = user
        self.password = password
        self.database = database
        self.conexao = None
        self.cursor = None

    def conectar(self):
        self.conexao = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database)

    def desconectar(self):
        self.conexao.close()        
        # Meu Servidor
        # host ='10.28.2.39',
        # user='suporte',
        # password='suporte',
        # database='biblioteca' 
