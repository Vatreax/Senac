import mysql.connector

class Usuario:
    def __init__(self,nome,cpf,senha,telefone):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.telefone = telefone

    def cadastrar_usuario(self):
        self.usuario_atributos = mysql.DataFrame({
            'nome':self.nome,
            'cpf':self.cpf,
            'senha':self.senha,
            'telefone':self.telefone
            })
        
    def create(self):
        return f'insert into usuario(nome, cpf, telefone) values("{self.nome}", "{self.cpf}", "{self.telefone}")'
    
    def read(self):
        return f'select * from usuario where cpf = "{self.cpf}"'
    
    def update(self):
        return f'update usuario set telefone = "{self.telefone}" where codigo = "{self.cpf}"'
    
    def delete(self):
        return f'delete from usuario where cpf = "{self.cpf}"'
    
Usuario.__name__ = "Usuario"