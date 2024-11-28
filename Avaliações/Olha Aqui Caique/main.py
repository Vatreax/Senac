import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

# from models.livros import Livro
# from models.usuario import Usuario
# livrin = Livro('auto','titulo','','')
# usando = Usuario('Tafarel','123456789','6799132323')
# print(vars(livrin))
# print(vars(usando))

while True:
    op = input("""
Opções
    1 - Cadastro Livro
    2 - Cadastro de Usuario
    3 - Empréstimo
    4 - Login
    0 - Sair
    - """)
    
    if op == "1":
        ui_file = "Avaliações/Atividade Python - 05_11_2024/views/Cadastro de Livro.ui"

        class MainWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                uic.loadUi(ui_file, self)
                self.Cadastrar.clicked.connect(self.clickedCadastro)
                self.Cancelar.clicked.connect(self.clickedCancelar)

            
            def clickedCancelar(self):
                print("Cancelado")
                self.close()

            def clickedCadastro(self):
                autor = self.Autor.text()
                titulo = self.Titulo.text()
                genero = self.Genero.text()
                codigo = self.Codigo.text()
                disponibilidade = self.Disponibilidade.currentText()

                print(f"""
        autor: {autor}
        titulo: {titulo}
        genero: {genero}
        codigo: {codigo}
        disponibilidade: {disponibilidade}""")


        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())

    if op == "2":
        ui_file = "Avaliações/Atividade Python - 05_11_2024/views/Cadastro de Usuario.ui"

        class MainWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                uic.loadUi(ui_file, self)
                self.Cadastrar.clicked.connect(self.clickedCadastrar)
                self.Cancelar.clicked.connect(self.clickedCancelar)

            
            def clickedCancelar(self):
                print("Cancelado")
                self.close()

            def clickedCadastrar(self):
                nome = self.Nome.text()
                senha = self.Senha.text()
                cpf = self.Cpf.text()
                telefone = self.Telefone.text()

                print(f"""
        Nome: {nome}
        Senha: {senha}
        CPF: {cpf}
        Telefone: {telefone}""")
                
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())

    if op == "4":
        ui_file = "Avaliações/Atividade Python - 05_11_2024/views/senha.ui"

        class MainWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                uic.loadUi(ui_file, self)
                self.Entrar.clicked.connect(self.clickedEntrar)
                self.Sair.clicked.connect(self.clickedSair)

            
            def clickedSair(self):
                print("Cancelado")
                self.close()

            def clickedEntrar(self):
                nome = self.Nome.text()
                senha = self.Senha.text()

                print(f"""
        Nome: {nome}
        Senha: {senha}
""")
                
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())

    if op == "0":
        break