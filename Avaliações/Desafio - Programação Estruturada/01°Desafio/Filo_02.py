from Reino_01 import Reino
class Filo(Reino):
    def __init__(self, nome_reino, multicelular, nome_filo,caracter_filo):
        super().__init__(nome_reino, multicelular)
        self.nome_filo     = nome_filo
        self.caracter_filo = caracter_filo