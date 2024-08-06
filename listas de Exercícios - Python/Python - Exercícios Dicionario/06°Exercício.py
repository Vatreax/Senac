palavras = {
    'Jejuar':'Significado: Ficar Por Um Determinado Tempo, Sem Comer.',
    'Agredir':'Significado: Ato de Causar Uma Lesão Fisica Em Outra Pessoa.',
    'Cachorro':'Significado: Animal, Canino De 4 Patas',
    'Arroz':'Significado: Alimento Em Grãos.',
    'Facilitar':'Significado: Tornar Mais Facil; Simplificar Algo.',
    'Cafuné':'Significado: Acariciar Algo/Alguem.',
    'Avariar':'Significado: Danificar um Objeto'
}

tradutor = input("Digite a Palavra: ").capitalize()
for i in palavras.items():
    if tradutor in i:
        print(i)