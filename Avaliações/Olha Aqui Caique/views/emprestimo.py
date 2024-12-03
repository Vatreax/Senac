import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

ui_file = "Avaliações/Olha Aqui Caique/views/emprestimo.ui"

class Emprestimo(QMainWindow):
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
    window = Emprestimo()
    window.show()
    sys.exit(app.exec_())