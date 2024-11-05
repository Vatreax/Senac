import mysql.connector
from atividade import connect_sql
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