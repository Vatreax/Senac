from Familia_05 import Familia
class Genero(Familia):
    def __init__(self, nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe, nome_ordem, caracter_ordem, nome_familia, caracter_familia,nome_genero):
        super().__init__(nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe, nome_ordem, caracter_ordem, nome_familia, caracter_familia)
        self.nome_genero = nome_genero