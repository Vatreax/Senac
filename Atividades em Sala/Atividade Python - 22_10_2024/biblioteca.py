from livros import Livro
from tarefa import Usuario

class Biblioteca:
    Acervo = []
    @staticmethod
    def emprestar(usuario: Usuario, livro: list[Livro]) -> bool:
        for item in livro:
            if len(usuario.lista_livros) == usuario.MAX_EMPRESTIMO:
                return
            item.emprestimo_livro(usuario)
            usuario.pegar_emprestado(item)

        return True
    # @staticmethod
    # def devolver(livro: Livros, usuario: Usuario):
        # livro.devolver_livro()
        # usuario