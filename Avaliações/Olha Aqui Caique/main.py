import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from models.livros import Livro
from models.usuario import Usuario

from views.login import Login_MainWindow
from views.usuario import Cadastro_Usuario





while True: 
    op = input("""Digite uma das opções
        1 - Login
        2 - Cadastrar Usuario
        3 - Cadastrar Livro
        4 - Empréstimo
        0 - Sair""")
    


    if op == "1":
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = Login_MainWindow()
            window.show()
            sys.exit(app.exec_())

        tela = Login_MainWindow()

    if op == "2":
        if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = Cadastro_Usuario()
            window.show()
            sys.exit(app.exec_())

        tela = Cadastro_Usuario()