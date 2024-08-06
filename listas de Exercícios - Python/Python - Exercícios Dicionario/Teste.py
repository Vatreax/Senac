contatinhos = {
    'Eletricista':'9912-3345',
    'Tia da Fofoca':'9933-8822',
    'Roberval':'9112-3322'
}

# Escreva o arquivo antes do 'r' para ler
#          |
#          |
#          V


with open('contatinhos.txt', 'w') as arquivo:
    for contato, n1 in contatinhos.items():
        arquivo.write(str(contato) + ' - ' + str(n1) + '\n')

# Após escrever o arquivo com o 'w', leia
#          |
#          |
#          V

with open('contatinhos.txt', 'r') as arquivo:
    for contatos in 'contatinhos.txt':
        arquivo.readlines
        for linhas in arquivo:
            print(linhas)