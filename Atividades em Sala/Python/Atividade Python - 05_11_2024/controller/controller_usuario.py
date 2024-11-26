from models.usuario import Usuario
from models.database import Database


class Controller_Usuario:

   def cadastrar_usuario(self):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      usuarios = Usuario('Jão do Bão','1122334455','67991295341')

      db.cursor.execute(usuarios.create())
      db.conexao.commit()
      db.desconectar()


   def procurar_usuario(self):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      usuarios = Usuario('','1122334455','')

      db.cursor.execute(usuarios.read())
      print(db.cursor.fetchall())
      db.conexao.commit()
      db.desconectar()


op = Controller_Usuario()
op.procurar_usuario()