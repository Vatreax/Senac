class Pessoa:
    def __init__(self,nome,idade,cpf,altura,peso):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.altura = altura
        self.peso = peso


class Estudante(Pessoa):
    def __init__(self,nome,cpf,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.altura = altura
        self.peso = peso

    def da_uma_printada(self):
        
        print(f"\nNome: {pessoa.nome}\nIdade: {pessoa.idade}\nCPF: {pessoa.cpf}\nAltura: {pessoa.altura} m \nPeso: {pessoa.peso} kg\n===========================")

pessoa = Estudante("Reginaldo",22,"111.222.333-44","1,76","70")
Estudante.da_uma_printada(1)