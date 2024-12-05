from datetime import date
class Cliente:

    def __init__(self, nome, cpf, endereco, telefone, data_nasc:date):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.data_nasc = data_nasc
    
    def calcular_idade(self):
        pass