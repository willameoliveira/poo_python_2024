from movimentacao import Movimentacao
from conta import Conta
from cliente import Cliente

movimentacao1 = Movimentacao(nome="Saque", valor=100)
print(movimentacao1)

cliente1 = Cliente(nome="José", cpf="233", endereco="Rua X", telefone="12", data_nasc=None)
conta1 = Conta(numero=12, saldo=200, cliente=cliente1)

movimentacao2 = Movimentacao(nome="Transferência", valor=100, conta_destino=conta1)
print(movimentacao2)