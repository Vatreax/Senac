import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

# from models.livros import Livro
# from models.usuario import Usuario
# livrin = Livro('auto','titulo','','')
# usando = Usuario('Tafarel','123456789','6799132323')
# print(vars(livrin))
# print(vars(usando))

ui_file = "Atividades em Sala/Python/Atividade Python - 05_11_2024/views/Cadastro de Livro.ui"

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