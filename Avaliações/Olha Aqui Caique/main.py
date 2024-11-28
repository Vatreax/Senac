import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from models.livros import Livro
from models.usuario import Usuario



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
        ui_file = "Avaliações/Olha Aqui Caique/views/Cadastro de Livro.ui"

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
        ui_file = "Avaliações/Olha Aqui Caique/views/Cadastro de Usuario.ui"

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
                confirmar_senha = self.Confirma_Senha.text()
                cpf = self.Cpf.text()
                telefone = self.Telefone.text()
                aviso = self.aviso

                if nome == "" or senha == "" or confirmar_senha == "" or cpf == "":
                    aviso.setStyleSheet("color:red")
                    aviso.setText("Todos os Campos Devem Ser Preenchidos!")

                else:
                    aviso.setStyleSheet("")
                    aviso.setText("")
                    print(f"""
            Nome: {nome}
            Senha: {senha}
            Confirmar Senha: {confirmar_senha}
            CPF: {cpf}
            Telefone: {telefone}""")
                
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            sys.exit(app.exec_())

    if op == "3":
        ui_file = "Avaliações/Olha Aqui Caique/views/emprestimo.ui"

        class MainWindow(QMainWindow):
            def __init__(self):
                super().__init__()
                uic.loadUi(ui_file, self)
                self.Registrar.clicked.connect(self.clickedRegistrar)
                self.Cancelar.clicked.connect(self.clickedCancelar)

            
            def clickedCancelar(self):
                print("Cancelado")
                self.close()

            def clickedRegistrar(self):
                autor = self.Autor.text()
                titulo = self.Titulo.text()
                genero = self.Genero.text()
                codigo = self.Codigo.text()
                disponibilidade = "indisponivel"
                aviso = self.aviso
               

                if autor == "" or titulo == "" or genero == "" or codigo == "":
                    aviso.setStyleSheet("color:red")
                    aviso.setText("Todos os Campos Devem Ser Preenchidos!")

                else:
                    aviso.setStyleSheet("")
                    aviso.setText("")
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

    if op == "4":
        ui_file = "Avaliações/Olha Aqui Caique/views/senha.ui"

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