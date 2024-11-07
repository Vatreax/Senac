class Livro:
    def __init__(self, autor, titulo, genero, cod_livro):
        self.autor = autor
        self.titulo = titulo
        self.genero = genero
        self.cod_livro = cod_livro

        self.status= 'Disponivel'
        self.usuario = None

    def create(self):
        return f'insert into livro(titulo, autor, genero, status, codigo) values("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", "{self.cod_livro}")'
        
       