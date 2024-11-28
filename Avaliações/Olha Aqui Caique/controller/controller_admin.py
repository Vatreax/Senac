from models.admin import Admin
from models.livros import Livro
from models.database import Database
from models.emprestimo import Emprestimo
from models.usuario import Usuario

# Cadastrar Usuario
# Cadastrar Livro
# Cadastrar Empréstimo


class Controller_Admin:

   # Interação Usuario
   def update_usuario(self):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      usuarios = Usuario('','1122334455','67991295341')

      db.cursor.execute(usuarios.update())
      db.conexao.commit()
      db.desconectar()

   def deletar_usuario(self):
      db = Database("10.28.2.39","suporte","suporte","biblioteca")
      db.conectar()
      
      usuarios = Usuario('','1122334455','')

      db.cursor.execute(usuarios.delete())
      db.conexao.commit()
      db.desconectar()


   # Interação Livro
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