from Especie_07 import Especie

animais = {
    #1° Animal
    "Onça-Pintada": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Caracteristica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica do Filo: Presença de glândulas mamárias", 
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Caracteristica da Ordem: Adaptações para dieta carnívora", 
    nome_familia="Familia: Felidae",
    caracter_familia="Característica da Familia: Presença de características felinas", 
    nome_genero="Gênero: Panthera",
    nome_especie="Espécie: Onca",),

    #2° Animal
    "Pinguim": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Aves",
    caracter_classe="Característica da Classe: Presença de penas, bico córneo e postura de ovos",
    nome_ordem="Ordem: Sphenisciformes",
    caracter_ordem="Característica da Ordem: Adaptados para a vida aquática, asas transformadas em nadadeiras",
    nome_familia="Família: Spheniscidae",
    caracter_familia="Característica da Família: Presença de características típicas dos pinguins, como penas impermeáveis e habilidades de mergulho",
    nome_genero="Gênero: Aptenodytes",
    nome_especie="Espécie: forsteri",
    ),

    #3° Animal
    "Capivara": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica do Filo: Presença de glândulas mamárias", 
    nome_ordem="Ordem: Rodentia",
    caracter_ordem="Característica da Ordem: Incisivos crescentes e adaptados para roer", 
    nome_familia="Família: Caviidae",
    caracter_familia="Característica da Família: Presença de características típicas dos caviídeos", 
    nome_genero="Gênero: Hydrochoerus",
    nome_especie="Espécie: hydrochaeris",
),

    #4° Animal
    "Aranha Marrom": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Arthropoda", 
    caracter_filo="Característica do Filo: Presença de exoesqueleto segmentado e apêndices articulados", 
    nome_classe="Classe: Arachnida",
    caracter_classe="Característica da Classe: Corpo dividido em duas regiões, cefalotórax e abdome, e ausência de antenas",
    nome_ordem="Ordem: Araneae",
    caracter_ordem="Característica da Ordem: Produção de seda para construção de teias e captura de presas",
    nome_familia="Família: Sicariidae",
    caracter_familia="Característica da Família: Presença de características típicas das aranhas do gênero Loxosceles, incluindo veneno necrosante",
    nome_genero="Gênero: Loxosceles",
    nome_especie="Espécie: reclusa",
    ),

    #5° Animal
    "Hipopótamo": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos (em algumas espécies)",
    nome_ordem="Ordem: Artiodactyla",
    caracter_ordem="Característica da Ordem: Pés ímpares com dois ou quatro dedos funcionais",
    nome_familia="Família: Hippopotamidae",
    caracter_familia="Característica da Família: Presença de características típicas dos hipopótamos, como corpo robusto e adaptado para a vida aquática",
    nome_genero="Gênero: Hippopotamus",
    nome_especie="Espécie: amphibius",
    ),

    #6° Animal
    "Canguru": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Diprotodontia",
    caracter_ordem="Característica da Ordem: Presença de incisivos inferiores alongados e grandes, adaptados para uma dieta herbívora",
    nome_familia="Família: Macropodidae",
    caracter_familia="Característica da Família: Presença de características típicas dos cangurus, como membros traseiros longos e fortes adaptados para o salto",
    nome_genero="Gênero: Macropus",
    nome_especie="Espécie: rufus",
    ),

    #7° Animal
    "Jiboia": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Reptilia",
    caracter_classe="Característica da Classe: Presença de escamas e oviparidade (na maioria das espécies)",
    nome_ordem="Ordem: Squamata",
    caracter_ordem="Característica da Ordem: Presença de escamas e língua bifurcada",
    nome_familia="Família: Boidae",
    caracter_familia="Característica da Família: Presença de características típicas das jiboias, como corpo robusto e habilidades de constricção. As serpentes dessa familia, são conhecidas por não serem peçonhentas",
    nome_genero="Gênero: Boa",
    nome_especie="Espécie: constrictor",
    ),

    #8° Animal
    "Tigre": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Característica da Ordem: Presença de dentes afiados e adaptados para alimentação carnívora",
    nome_familia="Família: Felidae",
    caracter_familia="Característica da Família: Presença de características típicas dos felinos, como garras retráteis e dentes caninos afiados",
    nome_genero="Gênero: Panthera",
    nome_especie="Espécie: tigris"
    ),

    #9° Animal
    "Papagaio" : Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Aves",
    caracter_classe="Característica da Classe: Presença de penas e oviparidade",
    nome_ordem="Ordem: Psittaciformes",
    caracter_ordem="Característica da Ordem: Presença de pés zigodáctilos e bico forte",
    nome_familia="Família: Psittacidae",
    caracter_familia="Característica da Família: Presença de características típicas dos papagaios, como capacidade de imitar sons e coloração vibrante",
    nome_genero="Gênero: Amazona",
    nome_especie="Espécie: aestiva"
    ),

    #10° Animal
    "Elefante": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Proboscidea",
    caracter_ordem="Característica da Ordem: Presença de tromba e presas",
    nome_familia="Família: Elephantidae",
    caracter_familia="Característica da Família: Presença de presas (nos elefantes machos) e grande porte corporal",
    nome_genero="Gênero: Loxodonta",
    nome_especie="Espécie: africana"
    ),

    #11° Animal
    "Orangotango": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Primates",
    caracter_ordem="Característica da Ordem: Presença de mãos preênseis e visão estereoscópica",
    nome_familia="Família: Hominidae",
    caracter_familia="Característica da Família: Presença de características típicas dos grandes símios, como inteligência avançada e braços longos",
    nome_genero="Gênero: Pongo",
    nome_especie="Espécie: pygmaeus"
    ),

    #12° Animal
    "Girafa": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Artiodactyla",
    caracter_ordem="Característica da Ordem: Presença de cascos e número par de dedos nas patas",
    nome_familia="Família: Giraffidae",
    caracter_familia="Característica da Família: Presença de pescoço longo e pernas compridas",
    nome_genero="Gênero: Giraffa",
    nome_especie="Espécie: camelopardalis"
    ),

    #13° Animal
    "Leão": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Característica da Ordem: Presença de dentes afiados e adaptados para alimentação carnívora",
    nome_familia="Família: Felidae",
    caracter_familia="Característica da Família: Presença de características típicas dos felinos, como garras retráteis e dentes caninos afiados",
    nome_genero="Gênero: Panthera",
    nome_especie="Espécie: leo"
    ),

    #14° Animal
    "Cavalo": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Perissodactyla",
    caracter_ordem="Característica da Ordem: Presença de cascos ímpares e adaptação para locomoção terrestre",
    nome_familia="Família: Equidae",
    caracter_familia="Característica da Família: Presença de cascos e crina na região dorsal",
    nome_genero="Gênero: Equus",
    nome_especie="Espécie: ferus caballus"
    ),

    #15° Animal
    "Golfinho": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Cetacea",
    caracter_ordem="Característica da Ordem: Presença de nadadeiras e adaptação ao ambiente aquático",
    nome_familia="Família: Delphinidae",
    caracter_familia="Característica da Família: Presença de corpo fusiforme e capacidade de comunicação vocal",
    nome_genero="Gênero: Tursiops",
    nome_especie="Espécie: truncatus"
    ),

    #16° Animal
    "Urso Polar": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Característica da Ordem: Presença de dentes afiados e adaptados para alimentação carnívora",
    nome_familia="Família: Ursidae",
    caracter_familia="Característica da Família: Presença de pelagem espessa e adaptação ao ambiente ártico",
    nome_genero="Gênero: Tursiops",
    nome_especie="Espécie: truncatus"
    ),

    #17° Animal
    "Rinoceronte": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Perissodactyla",
    caracter_ordem="Característica da Ordem: Presença de cascos ímpares e adaptação para locomoção terrestre",
    nome_familia="Família: Rhinocerotidae",
    caracter_familia="Característica da Família: Presença de chifres e corpo maciço",
    nome_genero="Gênero: Ceratotherium",
    nome_especie="Espécie: simum"
    ),

    #18° Animal
    "Gorila": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Primates",
    caracter_ordem="Característica da Ordem: Presença de mãos preênseis e visão estereoscópica",
    nome_familia="Família: Hominidae",
    caracter_familia="Característica da Família: Presença de características típicas dos grandes símios, como inteligência avançada e braços longos",
    nome_genero="Gênero: Gorilla",
    nome_especie="Espécie: gorilla"
    ),

    #19° Animal
    "Crocodilo": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Reptilia",
    caracter_classe="Característica da Classe: Presença de escamas e oviparidade (na maioria das espécies)",
    nome_ordem="Ordem: Crocodylia",
    caracter_ordem="Característica da Ordem: Presença de escamas e mandíbula poderosa",
    nome_familia="Família: Crocodylidae",
    caracter_familia="Característica da Família: Presença de corpo alongado e adaptação ao ambiente aquático",
    nome_genero="Gênero: Crocodylus",
    nome_especie="Espécie: porosus"
    ),

    #20° Animal
    "Macaco": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Primates",
    caracter_ordem="Característica da Ordem: Presença de mãos preênseis e visão estereoscópica",
    nome_familia="Família: Cercopithecidae",
    caracter_familia="Característica da Família: Presença de cauda preênsil e habilidade para locomoção arbórea",
    nome_genero="Gênero: Macaca",
    nome_especie="Espécie: fascicularis"
    ),

    #21° Animal
    "Tigre Branco": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Característica da Ordem: Presença de dentes afiados e adaptados para alimentação carnívora",
    nome_familia="Família: Felidae",
    caracter_familia="Característica da Família: Presença de características típicas dos felinos, como garras retráteis e dentes caninos afiados",
    nome_genero="Gênero: Panthera",
    nome_especie="Espécie: tigris"
    ),

    #22° Animal
    "Lobo": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Característica da Ordem: Presença de dentes afiados e adaptados para alimentação carnívora",
    nome_familia="Família: Canidae",
    caracter_familia="Característica da Família: Presença de características típicas dos lobos, como olfato aguçado e comportamento social",
    nome_genero="Gênero: Canis",
    nome_especie="Espécie: lupus"
    ),

    #23° Animal
    "Águia": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Aves",
    caracter_classe="Característica da Classe: Presença de penas e oviparidade",
    nome_ordem="Ordem: Accipitriformes",
    caracter_ordem="Característica da Ordem: Presença de bico curvo e garras afiadas",
    nome_familia="Família: Accipitridae",
    caracter_familia="Característica da Família: Presença de características típicas das águias, como visão aguçada e voo planado",
    nome_genero="Gênero: Aquila",
    nome_especie="Espécie: chrysaetos"
    ),

    #24° Animal
    "Cachorro-do-Mato": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Mammalia",
    caracter_classe="Característica da Classe: Presença de glândulas mamárias e pelos",
    nome_ordem="Ordem: Carnivora",
    caracter_ordem="Característica da Ordem: Presença de dentes afiados e adaptados para alimentação carnívora",
    nome_familia="Família: Canidae",
    caracter_familia="Característica da Família: Presença de características típicas dos cães, como olfato aguçado e sociabilidade com humanos",
    nome_genero="Gênero: Chrysocyon",
    nome_especie="Espécie: brachyurus"
    ),

    #25° Animal
    "Pica-Pau": Especie(
    nome_reino="Reino: Animal",
    multicelular="Organização Celular: Multicelular",
    nome_filo="Filo: Chordata", 
    caracter_filo="Característica do Filo: Presença de notocorda", 
    nome_classe="Classe: Aves",
    caracter_classe="Característica da Classe: Presença de penas e oviparidade",
    nome_ordem="Ordem: Piciformes",
    caracter_ordem="Característica da Ordem: Presença de bico alongado e adaptado para perfurar madeira",
    nome_familia="Família: Picidae",
    caracter_familia="Característica da Família: Presença de crista na cabeça e habilidade para escalar troncos",
    nome_genero="Gênero: Picus",
    nome_especie="Espécie: viridis"
    ),

}

while True:
    o_animal = input("""
Lista de Animais:

    - Capivara
    - Onça-Pintada
    - Pinguim
    - Aranha Marrom
    - Hipopótamo
    - Canguru
    - Jiboia
    - Tigre
    - Papagaio
    - Elefante
    - Orangotango
    - Girafa
    - Leão
    - Golfinho
    - Urso Polar
    - Rinoceronte
    - Gorila
    - Crocodilo
    - Macaco
    - Tigre Branco
    - Lobo
    - Águia
    - Cachorro-do-Mato
    - Pica-Pau

Digite o nome do Animal, para saber mais detalhes - """).title()
    for i, cont in animais.items():
        if o_animal in i:
            print()
            print(i)
            cont.da_uma_printada()
            print()
    n1 = input("""  Digite:
        [1] Para Continuar
        [2] Encerrar Sistema
        
        - """)
    
    if n1 == "2":
        print("\nTenha um Bom Dia (^-^)")
        break