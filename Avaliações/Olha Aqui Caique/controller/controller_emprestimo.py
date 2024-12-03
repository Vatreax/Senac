from models.database import Database
from models.emprestimo import Emprestimo
from models.usuario import Usuario
from models.livros import Livro

class Controller_Emprestimo:
    def emprestar(self,Emprestimo):
        db = Database("10.28.2.39","suporte","suporte","biblioteca")
        db.conectar()

    