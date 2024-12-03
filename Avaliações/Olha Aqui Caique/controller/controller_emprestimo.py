from models.database import Database
from models.emprestimo import Emprestimo

class Controller_Emprestimo:
    def emprestar(self,infoemprestimo):
        db = Database("10.28.2.39","suporte","suporte","biblioteca")
        db.conectar()

        emprestimo = Emprestimo(infoemprestimo['id_usuario'], infoemprestimo['id_usuario'])
        db.cursor.execute(emprestimo.create())
        db.conexao.commit()
        db.desconectar()

