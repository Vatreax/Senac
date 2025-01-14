print("""
===============================
|        Login e Senha        |
===============================
""")

nome = input("Digite o seu Nome: ")
senha = input("Digite a senha de Usuário: ")

while nome == senha:
    print("""
              
    Nome ou Senha Incorreto
            
    """)
    nome = input("Digite o seu Nome: ")
    senha = input("Digite a senha de Usuário: ")

if nome != senha: 

    print("""
          
    Login Realizado com sucesso
    """)