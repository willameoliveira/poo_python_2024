from datetime import datetime

class Movimentacao:
    
    def __init__(self, nome: str, valor: float, conta_destino=None, data = datetime.now()):
        self.nome = nome
        self.valor = valor
        self.conta_destino = conta_destino
        self.data = data

    def __str__(self):
        string = f"""{self.data.strftime('%d/%m/%y %H:%M')} - {self.nome} de R$ {self.valor}"""
        if self.nome == "Transferência":
            string += f" para conta {self.conta_destino.numero}: {self.conta_destino.cliente.nome}"
        return string
