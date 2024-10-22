from ordem import Carnivora
# 5 Familia
class Canideos(Carnivora):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada)
        self.territorialidade = territorialidade
        self.org_jacobson = org_jacobson
    
    def marcar_territorio(self):
        print("O canídeo está marcando seu território.")


