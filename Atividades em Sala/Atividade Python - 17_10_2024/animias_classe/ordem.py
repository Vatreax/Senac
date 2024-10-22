from classe import Mamiferos
# 4 Ordem
class Carnivora(Mamiferos):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas)
        self.caninos_molares = caninos_molares
        self.pelagem_peltada = pelagem_peltada

    def habilidade_caca(self):
        print("O carnívoro usa suas habilidades de caça para pegar presas.")



