# 1 - Reino
class Animal:
    def __init__(self, nome, nome_cientifico, nutricao, habitat):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.nutricao = nutricao
        self.habitat = habitat
        
    def alimentar(self):
        print("Comer...")

    def movimentar(self):
        print("Andou/Nadou/Voou...")

