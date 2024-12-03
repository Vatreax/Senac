from models.livros import Livro
from models.database import Database
from models.livros import *



class Controller_Livro:

   def cadastrar_livro(self, informacoesLivro):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      livros = Livro(informacoesLivro['autor'], informacoesLivro['titulo'], informacoesLivro['cod_livro'])

      db.cursor.execute(livros.create())
      db.conexao.commit()
      db.desconectar()



   def procurar_Livro(self, informacoesLivro):
      procurar = Database("10.28.2.39","suporte","suporte","biblioteca")
      procurar.conectar()

      livros = Livro()

      procurar.cursor.execute(livros.read())

      print(procurar.cursor.fetchall())

      procurar.desconectar()
   

op = Controller_Livro()
op.procurar_Livro()