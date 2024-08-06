from Filo_02 import Filo
class Classe(Filo):
    def __init__(self, nome_reino, multicelular, nome_filo, caracter_filo,nome_classe,caracter_classe):
        super().__init__(nome_reino, multicelular, nome_filo, caracter_filo)
        self.nome_classe = nome_classe
        self.caracter_classe = caracter_classe