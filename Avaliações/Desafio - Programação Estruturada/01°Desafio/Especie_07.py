from Genero_06 import Genero
class Especie(Genero):
    def __init__(self, nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe, nome_ordem, caracter_ordem, nome_familia, caracter_familia, nome_genero, nome_especie):
        super().__init__(nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe, nome_ordem, caracter_ordem, nome_familia, caracter_familia, nome_genero)
        self.nome_especie = nome_especie

    def da_uma_printada(self):
        print(self.nome_genero)
        print(self.nome_especie)
        print(self.nome_reino)
        print(self.multicelular)
        print(self.nome_filo)
        print(self.caracter_filo)
        print(self.nome_classe)
        print(self.caracter_classe)
        print(self.nome_ordem)
        print(self.caracter_ordem)
        print(self.nome_familia)
        print(self.caracter_familia)