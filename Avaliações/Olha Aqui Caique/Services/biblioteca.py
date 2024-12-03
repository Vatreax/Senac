import mysql.connector
# from main import Database
from models.usuario import Usuario
from controller.controller_admin import Controller_Admin
from controller.controller_usuario import Controller_Usuario
from controller.controller_livro import Controller_Livro

class Biblioteca:

    def emprestimo_livro(self, usuario: Usuario):
        if self.status!= 'disponivel':
            return

        self.usuario = usuario.nome
        self.status= "Indisponivel"

    def devolver_livro(self):
        if self.status!= 'Indisponivel':
                return 'Não'
        
        self.usuario = None
        self.status = 'Disponivel'
    @staticmethod
    def cadastrarUsuario(informacoesUsuario):
        Controller_Usuario().cadastrar_usuario(informacoesUsuario)

    @staticmethod
    def cadastrarLivro(informacoesLivro):
         Controller_Livro().cadastrar_livro(informacoesLivro)

Controller_Admin.__name__ = 'Biblioteca'