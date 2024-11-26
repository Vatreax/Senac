class Empresa:
    nome = "Renato Lanches"
    CNPJ = "12.123.321/0171-02"
    ramo = "Alimentício"
    def descrição(self):
        return self.nome, self.CNPJ, self.ramo

empresa = Empresa()
print(empresa.descrição())

class Pessoa:
    nome = "Roberval"
    CPF = "666.171.069-51"
    Altura = "1,71"
    Peso = "51"
    Ocupação = "Desempregado"

    def descrição_pessoa(self):
        return self.nome, self.CPF, self.Altura, self.Peso, self.Ocupação

pessoa = Pessoa()

print(pessoa.descrição_pessoa())