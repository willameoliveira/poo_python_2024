from movimentacao import Movimentacao 

class Conta:
    
    _total_contas = 0

    def __init__(self, numero:int, saldo:float, cliente:str):
      self.numero = numero
      self.saldo = saldo
      self.cliente = cliente
      self.movimentacao = []
      Conta._total_contas += 1

    def depositar(self, valor):
      if valor > 0:
         self.saldo += valor
         self.movimentacao.append(Movimentacao("Deposito", valor))

    def ver_saldo(self):
        print(f"numero da conta:{self.numero} | cliente:{self.cliente} | saldo:R${self.saldo}")
      
    def sacar(self, valor):
       if (valor <= self.saldo) :
          self.saldo -= valor
          self.movimentacao.append(Movimentacao("Saque", valor))
          return True
       else:
          return False
       
    def transferir(self,conta_destino, valor):
        if (valor <=self.saldo):
           self.saldo -= valor
           conta_destino.saldo += valor
           self.movimentacao.append(Movimentacao("Transferência enviada", valor, conta_destino))  
           conta_destino.movimentacao.append(Movimentacao("Transferência recebida", valor, self))
           return True
        else:
           return False
        
    def ver_extrato(self)-> list[Movimentacao]:
       return self.movimentacao
    
    @classmethod
    def get_total_contas(cls):
       return cls._total_contas
