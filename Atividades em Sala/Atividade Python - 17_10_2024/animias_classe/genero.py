from familia import Canideos
# 6 Gênero
class Vulpes(Canideos):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson, cauda_espessa, onivoro):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson)
        self.cauda_espessa = cauda_espessa
        self.onivoro = onivoro

    def adaptabilidade(self):
        print(f"A raposa do gênero Vulpes é altamente adaptável,\n conseguindo viver em diversos habitats, como:\n florestas, desertos e áreas urbanas.")

