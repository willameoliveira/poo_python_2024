from datetime import datetime
from cliente import Cliente

class Conta:
    
    def __init__(self, numero, saldo, cliente:Cliente=None, data_abertura=datetime.now()):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        self.data_abertura = data_abertura

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if (valor <= self.saldo):
            self.saldo -= valor
            return True
        else:
            return False
    
    def ver_saldo(self):
        print(f"Número: {self.numero}| Saldo: {self.saldo}")
    
    def transferir(self, conta_destino, valor):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            return True
        else:
            return False