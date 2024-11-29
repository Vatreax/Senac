import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from models.livros import Livro
from models.usuario import Usuario

from views.login import Login_MainWindow
from views.usuario import Cadastro_Usuario


    



if __name__ == '__main__':
            app = QApplication(sys.argv)
            window = Login_MainWindow()
            window.show()
            sys.exit(app.exec_())

tela = Login_MainWindow()