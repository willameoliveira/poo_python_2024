from datetime import date
class Cliente:

    def __init__(self, nome, cpf, endereco, telefone, data_nasc:date):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.telefone = telefone
        self.data_nasc = data_nasc
    
    def calcular_idade(self):
        hoje = date.today()
        dt_nasc = self.data_nasc
        idade = hoje.year - dt_nasc.year
        if hoje.month <= dt_nasc.month and hoje.day < dt_nasc.day:
            idade -= 1   
        return idade
