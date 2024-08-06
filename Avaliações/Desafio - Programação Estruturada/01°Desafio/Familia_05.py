from Ordem_04 import Ordem
class Familia(Ordem):
    def __init__(self, nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe, nome_ordem, caracter_ordem, nome_familia, caracter_familia):
        super().__init__(nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe, nome_ordem, caracter_ordem)
        self.nome_familia = nome_familia
        self.caracter_familia = caracter_familia
