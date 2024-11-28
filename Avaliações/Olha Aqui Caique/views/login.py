import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

ui_file = "Avaliações/Olha Aqui Caique/views/senha.ui"

class Login_MainWindow(QMainWindow):
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
        