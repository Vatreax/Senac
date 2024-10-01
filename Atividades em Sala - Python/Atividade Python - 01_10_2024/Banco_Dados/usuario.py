from db import Database

class Usuario:

    def __init__(self, db_name):
        self.db = Database(db_name)
        self.db.conectar()

    def criar_usuario(self,nome,email):
        query = 'INSERT INTO usuario (nome,email) VALUES (?,?)'
        self.db.executar(query,(nome, email))
        self.db.commit()

    def listar_usuario(self):
        query = 'SELECT * FROM usuario'
        self.db.executar(query)
        dados = self.db.fet_do_all()     
        return dados
    
    def atualizar_usuario(self, id, novoNome, novoEmail):
        query = "UPDATE usuario SET"
        parametros = []
        if novoNome:
            query += ' nome = ?'
            parametros.append(novoNome)
        if novoEmail:
            if parametros:
                query += ','
            query += ' email = ?'
            parametros.append(novoEmail)

        query = 'UPDATE usuario SET nome = ?, email = ? where id = ?'
        

    def deletar_usuario(self,id):
        query = 'DELETE FROM usuario WHERE id = ?'
        self.db.executar(query,(id,))
        self.db.commit()

user = Usuario('bancoDados.db')
user.criar_usuario('Rafael','rafasmontiel13@gmail.com')