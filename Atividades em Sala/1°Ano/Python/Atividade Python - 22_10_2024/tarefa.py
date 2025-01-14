class Usuario:
    MAX_EMPRESTIMO = 3
    def __init__(self,nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.lista_livros = []

    def pegar_emprestado(self,livro):
        if len(self.lista_livros) == self.MAX_EMPRESTIMO:
            return 'Limite de Empréstimo atingido.'
        
        self.lista_livros.append(livro.nome)
