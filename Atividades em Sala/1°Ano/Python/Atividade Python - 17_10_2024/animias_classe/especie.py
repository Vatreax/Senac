from genero import Vulpes
# 7 Espécie
class Raposa_Vermelha(Vulpes):
    def __init__(self, nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson, cauda_espessa, onivoro, adaptabilidade, laranja_avermelhada):
        super().__init__(nome, nome_cientifico, nutricao, habitat, nervoso_dorsal, endoesqueleto, mamarias, endotermicos, orelhas, caninos_molares, pelagem_peltada, territorialidade, org_jacobson, cauda_espessa, onivoro)
        self.adaptabilidade = adaptabilidade
        self.laranja_avermelhada = laranja_avermelhada

    def alimento(self):
        print("A raposa-vermelha é Onivora, o que a torna capaz de se adaptar a maioria dos ambientes, incluido o urbano")



raposa = Raposa_Vermelha(
    nome="Raposa-vermelha",
    nome_cientifico="Vulpes vulpes",
    nutricao="Onívoro",
    habitat="Diversos (Urbano,Floresta,Deserto...)",
    nervoso_dorsal=True,
    endoesqueleto=True,
    mamarias=True,
    endotermicos=True,
    orelhas=True,
    caninos_molares=True,
    pelagem_peltada=True,
    territorialidade=True,
    org_jacobson=True,
    cauda_espessa=True,
    onivoro=True,
    adaptabilidade="Alta",
    laranja_avermelhada="Laranja-avermelhada"
)

print("1 - Animal: ")
Raposa_Vermelha.alimentar(raposa)
Raposa_Vermelha.movimentar(raposa)
print("\n2 - Filo: ")
Raposa_Vermelha.caracteristicas_filo(raposa)
print("\n3 - Classe: ")
Raposa_Vermelha.amamentar(raposa)
print("\n4 - Ordem: ")
Raposa_Vermelha.habilidade_caca(raposa)
print("\n5 - Familia: ")
Raposa_Vermelha.marcar_territorio(raposa)
print("\n6 - Genero: ")
Raposa_Vermelha.adaptabilidade(raposa)
print("\n7 - Espécie:")
Raposa_Vermelha.alimento(raposa)

print(f"""\n\n
+===============================================+
| Nome: {raposa.nome}                         |
| Nome Científico: {raposa.nome_cientifico}                |
+=============== CARACTERISTICAS ===============+
| {raposa.nutricao}                              
| {raposa.habitat} 
| {'Nervoso Dorsal' if raposa.nervoso_dorsal else None}                    
| {'Endoesqueleto' if raposa.endoesqueleto else None}                              
| {'Mamifero' if raposa.mamarias else None}                                       
| {'Endotérmico' if raposa.endotermicos else None}                                                
| {'Caninos/Molares' if raposa.orelhas else None}                                           
| {'Caninos/Molares' if raposa.caninos_molares else None}              
| {'Pelagem Peltada' if raposa.pelagem_peltada else None}              
| {'Territorial' if raposa.territorialidade else None}         
| {'Orgão Jacobson' if raposa.org_jacobson else None}             
| {'Cauda Espessa' if raposa.cauda_espessa else None}                
| {'Adaptabilidade' if raposa.adaptabilidade else None}              
| Cor {raposa.laranja_avermelhada}                      
+================================================+
""")