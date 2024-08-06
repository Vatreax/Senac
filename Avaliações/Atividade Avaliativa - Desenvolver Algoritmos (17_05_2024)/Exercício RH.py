i = 0
while i == 0:
    nome_completo = input("Seu Nome: ")

    idade = int(input("Sua Idade: "))

    if idade >= 18:
        print("\nParabèns Você Passou Para a Próxima Fase!!\n")
    elif idade < 18:
        print("\nObrigado Pela Sua Participação!!\n")
        break

    cargo = int(input("""Cargo Disponíveis:
1) Administração 
2) Atendimento ao Cliente
3) Segurança
4) Gestor de Estoque

Digite o Número da Opcção:
"""))
    curso = input("\nTem Algum Curso de Qualificação na Área? S/N?")

    if curso == "S" or curso == "s":
        print("\nParabèns Você Passou Para a Próxima Fase!!\n")
        

    elif curso == "N" or curso == "n":
        print("\nObrigado Pela Sua Participação!!\n")
        break

    nota = float(input("Qual a Sua Nota na Avaliação: "))

    if nota >= 7:
        print("\nParabèns Você Passou Para a Próxima Fase!!\n")
    
    elif nota < 7:
        print("\nObrigado Pela Sua Participação!!\n")
        break

    i =+ 1
