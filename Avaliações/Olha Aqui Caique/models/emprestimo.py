from livros import Livro
from usuario import Usuario

class Emprestimo:
    def __init__(self, id_livro, id_usuario):
        self.id_livro = id_livro
        self.id_usuario = id_usuario
    
    def emprestado(self, id_livro):
       return (f"SELECT status FROM livro WHERE id_livro = %s", (id_livro,))
    
