import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

ui_file = "Atividades em Sala/Atividade Python - 05_11_2024/views/Cadastro de Livro.ui"

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