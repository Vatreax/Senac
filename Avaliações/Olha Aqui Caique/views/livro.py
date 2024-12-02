import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

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
        informacoesLivro = {
            "autor": self.Autor.text(),
            "titulo": self.Titulo.text(),
            "genero": self.Genero.text(),
            "codigo": self.codigo.text(),
            "disponibilidade": self.Disponibilidade.text()
        }


        if informacoesLivro['autor'] == "" or informacoesLivro["titulo"] == "" or informacoesLivro["disponibilidade"] == "" or informacoesLivro["codigo"] == "" or informacoesLivro["genero"] == "":
            aviso.setStyleSheet("color:red")
            aviso.setText("Todos os Campos Devem Ser Preenchidos!")

        else:

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