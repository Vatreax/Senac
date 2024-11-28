import mysql.connector
# from main import Database
from models.usuario import Usuario
from models.livros import Livro
from controller.controller_admin import Controller_Admin
from controller.controller_usuario import Controller_Usuario

class Biblioteca:

    @staticmethod
    def cadastrar_livro(self,titulo,autor,genero,status,codigo ):
        Controller_Admin.cadastro_livro(titulo,autor,genero,status,codigo);

        self.livro_atributos = mysql.DataFrame()
        
    def emprestimo_livro(self, usuario: Usuario):
        if self.status!= 'disponivel':
            return

        self.usuario = usuario.nome
        self.status= "Emprestado"

    def devolver_livro(self):
        if self.status!= 'Emprestado':
                return 'Não'
        
        self.usuario = None
        self.status = 'Disponivel'
    @staticmethod
    def cadastrarUsuario(informacoesUsuario):
        Controller_Usuario().cadastrar_usuario(informacoesUsuario)

Controller_Admin.__name__ = 'Biblioteca'