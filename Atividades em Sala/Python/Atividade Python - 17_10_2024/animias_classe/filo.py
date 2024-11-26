from reino import Animal
# 2 Filo
class Chordata(Animal):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto):
        super().__init__(nome, nome_cientifico, nutricao, habitat)
        self.nervoso_dorsal = nervoso_dorsal
        self.endoesqueleto = endoesqueleto

    def caracteristicas_filo(self):
        print("O filo Chordata é caracterizado pela presença de um nervoso dorsal,\n um endoesqueleto e estruturas relacionadas ao sistema nervoso,\n fundamentais para a classificação dos organismos desse grupo.")


