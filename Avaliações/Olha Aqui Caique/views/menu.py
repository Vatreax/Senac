import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from views.usuario import Cadastro_Usuario
from views.livro import livrando_livro
from views.emprestimo import Emprestimo

ui_file = "Avaliações/Olha Aqui Caique/views/menu.ui"

class Menu_biblioteca(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.usuario.clicked.connect(self.clickedUsuario)
        self.cadastrar_livro.clicked.connect(self.clickedCadastrarLivro)
        self.emprestimo.clicked.connect(self.clickedEmprestimo)


    def clickedUsuario(self):
        self.usuario = Cadastro_Usuario()
        self.usuario.show()
        self.close()

    def clickedCadastrarLivro(self):
        self.livro = livrando_livro()
        self.livro.show()
        self.close()

    def clickedEmprestimo(self):
        self.emprestado = Emprestimo()
        self.emprestado.show()
        self.close()
        



# window = Menu_biblioteca()
# window.show()
Menu_biblioteca.__name__ = "Menu_biblioteca"
