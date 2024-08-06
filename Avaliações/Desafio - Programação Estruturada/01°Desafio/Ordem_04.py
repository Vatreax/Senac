from Classe_03 import Classe
class Ordem(Classe):
    def __init__(self, nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe,nome_ordem,caracter_ordem):
        super().__init__(nome_reino, multicelular, nome_filo, caracter_filo, nome_classe, caracter_classe)
        self.nome_ordem = nome_ordem
        self.caracter_ordem = caracter_ordem