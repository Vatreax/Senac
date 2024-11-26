class Pessoa:
    Nome = "Erinéia"
    CPF = "151.616.212-51"
    Idade = 42
    Altura = "1.69"
    Peso = "55"
    
    def Velha():
        return False
    
    def Mãe():
        return True
    
    def Descrição_Pessoa(self):
        return self.Nome, self.CPF, self.Idade, self.Altura, self.Peso

pessoa = Pessoa()
print(pessoa.Descrição_Pessoa())

class Estudante:
    Nome = "Lindsey"
    Idade = 13
    Ano = "9°"
    Turma = "B"
    Escola = "E.E Cabo da Ciolo"

    def Desocupado():
        return True
    
    def Fofoqueiro():
        return True
    
    def Descrição_Estudante(self):
        return self.Nome, self.Idade, self.Ano, self.Turma, self.Escola

estudante = Estudante()
print(estudante.Descrição_Estudante())

class Trabalhador:
    Nome = "Janete Empreguete"
    CPF = "111.222.333-44"
    Moradia = "Kitinet"
    Habilidade = "Pagar Boleto"
    Salário = 1200.00

    def Trabalhar():
        return True
    
    def Férias():
        return False
    
    def Descrição_Trabalhador(self):
        return self.Nome, self.CPF, self.Moradia, self.Habilidade, self.Salário

trabalhador = Trabalhador()
print(trabalhador.Descrição_Trabalhador())
