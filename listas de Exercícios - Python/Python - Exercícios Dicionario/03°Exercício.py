contatinhos = {
    'Eletricista':'9912-3345',
    'Tia da Fofoca':'9933-8822',
    'Roberval':'9112-3322'
}
while True:
    açao = input("""
======= LISTA TELEFÔNICA =======
Selecione A Operação Desejada:
|1|Adicionar Contato
|2|Remover Contato
|3|Lista Telefónica
|4|Fechar Sistema

-""")
    
    if açao == "4":
        print("Tenha Um Bom Dia <3")
        break

    elif açao == "3":
        print("\n----- Contatos -----\n",contatinhos,"\n------------")

    elif açao == "2":
        delet = input("Digite o Nome do Contato: ").capitalize()
        for i in contatinhos:
            if delet in i:
                print(i)
                del contatinhos[i]
                break
    
    elif açao == "1":
        ad = input("Digite o Nome do Contato: ")
        ad_num = input("Digite o Número do Contato: ")
        contatinhos.update({ad:ad_num})