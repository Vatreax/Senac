from filo import Chordata
# 3 Classe
class Mamiferos(Chordata):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto)
        self.mamarias = mamarias
        self.endotermicos = endotermicos
        self.orelhas = orelhas

    def amamentar(self):
        print("A mamífera está amamentando os filhotes.")

