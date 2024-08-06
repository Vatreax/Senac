prod = {
    'café':[20],
    'pão':[10],
    'Bat-Leite':[5],
    'Bat-Sanduiche':[12],
    'Maçã':[15],
    'Banana':[22]
}

while True:
    açao = input("""
====== CONTROLE DE ESTOQUE ======
+===============================+
|  Código  |      Operação      |
|----------+--------------------|
|     E    | Atualizar Estoque  |
|----------+--------------------|
|     S    | Adicionar Produtos |
|----------+--------------------|
|     R    | Consultar Estoque  |
|----------+--------------------|
|     X    |       Sair         |
+===============================|

Digite o Código Da Operação: """)
    
    if açao == "X" or açao == "x":
        print("Tenha um Bom Dia :3")
