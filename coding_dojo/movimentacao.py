from datetime import datetime

class Movimentacao:

    def __init__(self, descricao: str, valor: float, conta_destino = None, data = datetime.now()):
        self.descricao = descricao
        self.data = data
        self.valor = valor
        self.conta_destino = conta_destino
    
    def __str__(self):
        string = f"""{self.data.strftime ('%d/%m %H:%M')} - {self.descricao} de R$ {self.valor}"""
        if self.descricao == "Transferência enviada":
            string += f" para conta {self.conta_destino.numero}"
        elif self.descricao == "Transferência recebida":
            string += f" da conta {self.conta_destino.numero}" 
        
        return string 
        
