while True:
    dicio = {
        'ola':'bom dia!',
        'tchau':'adeus',
    }
    print(dicio)
    try:
        n1 = input("Digite a Chave do Dicionário:")
        print(dicio[n1])
        break

    except KeyError:
        print("Essa Chave Não Existe")