import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from views.usuario import Cadastro_Usuario
from views.livro import livrando_livro
from views.emprestimo import emp

ui_file = "Avaliações/Olha Aqui Caique/views/menu.ui"

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.usuario.clicked.connect(self.clickedUsuario)
        self.cadastrar_livro.clicked.connect(self.clickedCadastrar_Livro)
        self.emprestimo.clicked.connect(self.clickedEmprestimo)


        def clickedUsuario(self):
            self.close()
            
