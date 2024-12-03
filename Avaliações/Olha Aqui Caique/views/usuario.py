import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *

from Services.biblioteca import Biblioteca
from views.menu import Menu

ui_file = "Avaliações/Olha Aqui Caique/views/Cadastro de Usuario.ui"

class Cadastro_Usuario(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(ui_file, self)
        self.Cadastrar.clicked.connect(self.clickedCadastrar)
        self.Cancelar.clicked.connect(self.clickedCancelar)

    
    def clickedCancelar(self):
        print("Cancelado")
        self.close()

    def clickedCadastrar(self):
        informacoesUsuario = {
            "nome" : self.Nome.text(),
            "senha" : self.Senha.text(),
            "confirmar_senha" : self.Confirma_Senha.text(),
            "cpf" : self.Cpf.text(),
            "telefone" : self.Telefone.text(),
        }
        aviso = self.aviso

        
        if informacoesUsuario['nome'] == "" or informacoesUsuario['senha'] == "" or informacoesUsuario['confirmar_senha'] == "" or informacoesUsuario['cpf'] == "" or informacoesUsuario['telefone'] == "":
            aviso.setStyleSheet("color:red")
            aviso.setText("Todos os Campos Devem Ser Preenchidos!")

        else:
            Biblioteca.cadastrarUsuario(informacoesUsuario)
            aviso.setStyleSheet("")
            aviso.setText("")
            print(f"""
    Nome: {informacoesUsuario['nome']}
    Senha: {informacoesUsuario['senha']}
    Confirmar Senha: {informacoesUsuario['confirmar_senha']}
    CPF: {informacoesUsuario['cpf']}
    Telefone: {informacoesUsuario['telefone']}""")
            self.close()
            Menu()
            