class pobre(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        print("Seu Pobre")


class tentativa():
    while True:
        try:
            salario = float(input("O quão pobre você é? Digite seu salário: "))
            if salario <= 1200:
                raise pobre()
            elif salario > 1200:
                print("\nVocê será Taxadd!\n")
                break
        
        except ValueError:
            print("\nValor Inválido! \n")
        
        except pobre:
            pass
