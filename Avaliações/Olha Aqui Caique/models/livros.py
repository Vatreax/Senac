import mysql.connector
class Livro:
    def __init__(self, autor, titulo, genero, cod_livro):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.cod_livro = cod_livro
        self.status= 'Disponivel'
        self.usuario = None

    def cadastrarLivro(self):
            self.livro_atributo = mysql.DataFrame({
            'titulo':self.titulo,
            'autor':self.autor,
            'genero':self.genero,
            'codigo':self.codigo
            })

    def create(self):
        return f'insert into livro(titulo, autor, genero, status, codigo) values("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", {self.cod_livro})'
    
    def read(self):
        return f'select * from livro where codigo = {self.cod_livro})'
    
    def update(self):
        return f'update livro set titulo = "{self.titulo}" where codigo = {self.cod_livro}'
    
    def delete(self):
        return f'delete from livro where codigo = {self.cod_livro}'
    

Livro.__name__ = "Livro"