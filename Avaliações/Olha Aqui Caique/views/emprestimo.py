import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from Services.biblioteca import Biblioteca

ui_file = "Avaliações/Olha Aqui Caique/views/emprestimo.ui"

class Emprestimo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.Registrar.clicked.connect(self.clickedRegistrar)
        self.Cancelar.clicked.connect(self.clickedCancelar)
    
    def clickedCancelar(self):
        print("Cancelado")
        from views.menu import Menu_biblioteca
        self.menu = Menu_biblioteca()
        self.menu.show()
        self.close()

    def clickedRegistrar(self):
        informacoesEmprestimo = {
        'cpf': self.Cpf.text(),
        'codigo': self.Codigo.text()
        }
        aviso = self.aviso

        if informacoesEmprestimo['cpf'] == "" or informacoesEmprestimo['codigo'] == "":
            aviso.setStyleSheet("color:red")
            aviso.setText("Todos os Campos Devem Ser Preenchidos!")

        else:
            Biblioteca.verficarEmprestimo(informacoesEmprestimo)
            aviso.setStyleSheet("")
            aviso.setText("")
            print(f"""
        cpf: {informacoesEmprestimo['cpf']}
        codigo: {informacoesEmprestimo['codigo']}""")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Emprestimo()
    window.show()
    sys.exit(app.exec_())