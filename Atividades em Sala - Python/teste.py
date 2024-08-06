import random

roleta = []

def fun_roleta ():
    while True:
        n1 = random.randint (1,75)
        if len(roleta) > 1:
            if n1 not in roleta:
                roleta.append(n1)
            else:
                continue
        else:
            roleta.append(n1)
        
        print("\n",roleta)
        break

def fun_cartela():
    global dicionario
    dicionario = {
    'B':[],
    'I':[],
    'N':[],
    'G':[],
    'O':[]
    }   

    
    while len(dicionario['B']) <= 5:
        num_random = random.randint (1,15)
        dicionario['B'].append(num_random)
            
    while len(dicionario['I'] ) <= 5:
        num_random = random.randint (15,30)
        dicionario['I'].append(num_random)

    while len(dicionario['N'] ) <= 5:
        num_random = random.randint (30,45)
        dicionario['N'].append(num_random)
        len(dicionario['N'])

    while len(dicionario['G'] ) <= 5:
        num_random = random.randint (45,60)
        dicionario['G'].append(num_random)

    while len(dicionario['O'] ) <= 5:
        num_random = random.randint (60,75)
        dicionario['O'].append(num_random)


fun_cartela()
print(dicionario)
































import random

def fun_cartela():
    cartela = {
        'B': [],
        'I': [],
        'N': [],
        'G': [],
        'O': []
    }

    # Preenchendo cada coluna da cartela com números aleatórios
    for letra in cartela:
        inicio = 1
        fim = 15 if letra != 'N' else 14  # A coluna N tem 14 números, então ajustamos o fim
        while len(cartela[letra]) < 5:
            num_random = random.randint(inicio, fim)
            if num_random not in cartela[letra]:  # Evita números duplicados na mesma coluna
                cartela[letra].append(num_random)

    return cartela

def formatar_cartela(cartela):
    # Cabeçalho da cartela
    cartela_formatada = " B   I   N   G   O\n"
    
    # Montando as linhas da cartela
    for i in range(5):
        linha = ""
        for letra in ['B', 'I', 'N', 'G', 'O']:
            if i < len(cartela[letra]):
                linha += f"{cartela[letra][i]:2d}  "
            else:
                linha += "    "  # Caso não haja número na posição
        cartela_formatada += linha.strip() + "\n"  # Adiciona a linha e remove o espaço extra do final

    return cartela_formatada

# Criando a cartela
cartela = fun_cartela()

# Formatando e imprimindo a cartela
cartela_formatada = formatar_cartela(cartela)
print(cartela_formatada)









































import random

def fun_cartela():
    cartela = {
        'B': [],
        'I': [],
        'N': [],
        'G': [],
        'O': []
    }

    # Preenchendo cada coluna da cartela com números aleatórios
    for letra in cartela:
        inicio = 1
        fim = 15 if letra != 'N' else 14  # A coluna N tem 14 números, então ajustamos o fim
        while len(cartela[letra]) < 5:
            num_random = random.randint(inicio, fim)
            if num_random not in cartela[letra]:  # Evita números duplicados na mesma coluna
                cartela[letra].append(num_random)

    return cartela

def formatar_cartela(cartela):
    cartela_formatada = ""
    
    # Cabeçalho da cartela
    cartela_formatada += "+---+---+---+---+---+\n"
    cartela_formatada += "| B | I | N | G | O |\n"
    cartela_formatada += "+---+---+---+---+---+\n"
    
    # Montando as linhas da cartela
    for i in range(5):
        linha = "|"
        for letra in ['B', 'I', 'N', 'G', 'O']:
            if i < len(cartela[letra]):
                linha += f" {cartela[letra][i]:2d} |"
            else:
                linha += "    |"  # Caso não haja número na posição
        cartela_formatada += linha + "\n"
        cartela_formatada += "+---+---+---+---+---+\n"

    return cartela_formatada

# Criando a cartela
cartela = fun_cartela()

# Formatando e imprimindo a cartela
cartela_formatada = formatar_cartela(cartela)
print(cartela_formatada)