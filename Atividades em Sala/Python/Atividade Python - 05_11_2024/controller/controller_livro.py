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
   
   def atualizar_Livro(self):
      atualizar = Database("10.28.2.39","suporte","suporte","biblioteca")
      atualizar.conectar()

      livros = Livro("um autor ai","Um titulo ai", "trans?", "15" )

      atualizar.cursor.execute(livros.update())
      atualizar.conexao.commit()
      atualizar.desconectar()

   
   def excluir_Livro(self):
      excluindo = Database("10.28.2.39","suporte","suporte","biblioteca")
      excluindo.conectar()

      livros = Livro("um autor ai","Um titulo ai", "trans?", "15" )

      excluindo.cursor.execute(livros.delete())
      excluindo.conexao.commit()
      excluindo.desconectar()

      
op = Controller_Livro()
op.procurar_Livro()