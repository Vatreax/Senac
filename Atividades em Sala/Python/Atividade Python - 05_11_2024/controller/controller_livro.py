from models.livros import Livro
from models.database import Database



class Controller_Livro:

   def cadastrar_livro(self):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      livros = Livro("um autor ai","Um titulo ai", "trans?", "15" )

      db.cursor.execute(livros.create())
      db.conexao.commit()
      db.desconectar()



   def procurar_Livro(self):
      procurar = Database("10.28.2.39","suporte","suporte","biblioteca")
      procurar.conectar()

      livros = Livro("um autor ai","Um titulo ai", "trans?", "15" )

      procurar.cursor.execute(livros.read())

      print(procurar.cursor.fetchall())

      procurar.desconectar()
   

op = Controller_Livro()
op.procurar_Livro()