import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from Services.biblioteca import Biblioteca


ui_file = "Avaliações/Olha Aqui Caique/views/Cadastro de Livro.ui"

class livrando_livro(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.Cadastrar.clicked.connect(self.clickedCadastro)
        self.Cancelar.clicked.connect(self.clickedCancelar)

    
    def clickedCancelar(self):
        print("Cancelado")
        from views.menu import Menu_biblioteca
        self.menu = Menu_biblioteca()
        self.menu.show()
        self.close()

    def clickedCadastro(self):
        informacoesLivro = {
            "autor": self.Autor.text(),
            "titulo": self.Titulo.text(),
            "genero": self.Genero.text(),
            "codigo": self.Codigo.text(),
            "disponibilidade": self.Disponibilidade
        }
        aviso = self.aviso



        if informacoesLivro['autor'] == "" or informacoesLivro["titulo"] == "" or informacoesLivro["disponibilidade"] == "" or informacoesLivro["codigo"] == "" or informacoesLivro["genero"] == "":
            aviso.setStyleSheet("color:red")
            aviso.setText("Todos os Campos Devem Ser Preenchidos!")

        else:
            Biblioteca.cadastrarLivro(informacoesLivro)
            aviso.setStyleSheet("")
            aviso.setText("")
            print(f"""
    autor: {informacoesLivro['autor']}
    titulo: {informacoesLivro['titulo']}
    genero: {informacoesLivro['genero']}
    codigo: {informacoesLivro['codigo']}
    disponibilidade: {informacoesLivro['disponibilidade']}""")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = livrando_livro()
    window.show()
    sys.exit(app.exec_())