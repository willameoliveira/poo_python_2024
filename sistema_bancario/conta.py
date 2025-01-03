from datetime import datetime
from cliente import Cliente
from movimentacao import Movimentacao

class Conta:
    
    def __init__(self, numero, saldo, cliente:Cliente, data_abertura=datetime.now()):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente
        self.data_abertura = data_abertura
        self.movimentacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.movimentacoes.append(Movimentacao("Depósito", valor))
    
    def sacar(self, valor):
        if (valor <= self.saldo):
            self.saldo -= valor
            self.movimentacoes.append(Movimentacao("Saque", valor))
            return True
        else:
            return False
    
    def ver_saldo(self):
        print(f"Número: {self.numero}| Saldo: {self.saldo}")
    
    def transferir(self, conta_destino, valor):
        if (valor <= self.saldo):
            self.saldo -= valor
            conta_destino.saldo += valor
            self.movimentacoes.append(Movimentacao("Transferência enviada", valor, conta_destino))
            conta_destino.movimentacoes.append(Movimentacao("Transferência recebida", valor, self))
            return True
        else:
            return False
    
    def ver_extrato(self) -> list[Movimentacao]:
        return self.movimentacoes