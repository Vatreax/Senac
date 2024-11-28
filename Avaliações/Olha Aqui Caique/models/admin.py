from models.usuario import Usuario

class Admin(Usuario):
    def __init__(self, nome, cpf, telefone, admin):
        super().__init__(nome, cpf, telefone)
        self.admin = admin

Admin.__name__ = 'Admin'