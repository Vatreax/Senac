from tarefa import Usuario
class Livro:
    def __init__(self, autor, nome, genero, cod_livro):
        self.autor = autor
        self.nome = nome
        self.genero = genero
        self.cod_livro = cod_livro
        self.status= 'Disponivel'
        self.usuario = None

    def emprestimo_livro(self, usuario: Usuario):
        if self.status!= 'disponivel':
            return

        self.usuario = usuario.nome
        self.status= "Emprestado"

    def devolver_livro(self):
        if self.status!= 'Emprestado':
                return 'Não'
        
        self.usuario = None
        self.status = 'Disponivel'



# while True:
#     op = input("""
#                Opções
#           |1|Cadastrar Usuario
#           |2|Print Usuarios
#           |0|Sair
#         -""")

#     if op == '1':
#         n1 = input("Digite o seu Nome: ")
#         n2 = input("Digite o seu Email: ")
#         n3 = input("Digite sua Senha")
#         Users.update({n1:Usuario(n1,n2,n3)})

#     if op == '2':
#         for i,  in Users:
#             print(vars(i))

#     if op == '0':
#         print("Tenha um Bom Dia. (^-^)")
#         break

