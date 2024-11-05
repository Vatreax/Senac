import mysql.connector
from atividade import Database
from usuario import usuario

class biblioteca:
    def __init__(self, titulo, autor, genero, status, codigo):
        self.livros_atributos = None
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.status = status
        self.codigo = codigo

    def livrando_livro(self):
        self.livro_atributos = mysql.DataFrame({
            'titulo':self.titulo,
            'autor':self.autor,
            'genero':self.genero,
            'status':self.status,
            'codigo':self.codigo})
        
    def emprestimo_livro(self, usuario: usuario):
        if self.status!= 'disponivel':
            return

        self.usuario = usuario.nome
        self.status= "Emprestado"

    def devolver_livro(self):
        if self.status!= 'Emprestado':
                return 'Não'
        
        self.usuario = None
        self.status = 'Disponivel'

class Controller_Livro:
     def cadastrar_livro():
        db = Database()
        db.conectar()
        livro = biblioteca()
        livro.create()

        db.cursor.execute()