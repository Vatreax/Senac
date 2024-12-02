import mysql.connector
# from main import Database
from models.usuario import Usuario
from models.livros import Livro
from controller.controller_admin import Controller_Admin
from controller.controller_usuario import Controller_Usuario
from views.livro import livrando_livro
from controller.controller_livro import Controller_Livro

class Biblioteca:

    @staticmethod
    def cadastrar_livro(self,titulo,autor,genero,status,codigo ):
        Controller_Admin.cadastro_livro(titulo,autor,genero,status,codigo);

        self.livro_atributos = mysql.DataFrame()
        
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