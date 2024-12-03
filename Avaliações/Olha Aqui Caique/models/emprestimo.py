class Emprestimo:
    def __init__(self, codigo, cpf):
        self.codigo = codigo
        self.cpf = cpf
    
    @staticmethod
    def emprestado(codigo):
       return (f"SELECT status FROM livro WHERE codigo = {codigo}")
    
    @staticmethod
    def usuario(cpf):
        return (f"SELECT id_usuario FROM usuario WHERE id_usuario = {cpf}")
    
    @staticmethod
    def cadastrar(cpf, codigo):
        return (f"Insert into emprestimo(cpf, codigo) values({cpf, codigo})")
