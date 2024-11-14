class Conta:
    # construtor da classe. Ele cria os objetos da classe
    def __init__(self, numero, saldo, data_abertura):
        self.numero = numero
        self.saldo = saldo
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