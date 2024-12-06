from conta import Conta
from cliente import Cliente
from datetime import datetime, date
import os

os.system("clear")

def teste_data_abertura():
    conta = Conta(1, 100, None) #Passando None (Nada), como cliente. Pois ele não é necessário nesse teste.
    print(f"Data abertura conta 1 é: {conta.data_abertura}")

    conta2 = Conta(2, 100, None, datetime.fromisoformat("2023-11-20T08:30:00"))
    print(f"Data abertura conta 2 é: {conta2.data_abertura}")

def teste_transferencia():
    conta = Conta(1, 100, None)
    conta2 = Conta(2, 100, None)

    if conta.transferir(conta2, 110):
        print("Transferência realizada com sucesso!")
    else:
        print("Transferência falhou. Saldo insuficiente!")

    conta.ver_saldo()
    conta2.ver_saldo()

def teste_conta_com_cliente():
    cliente1 = Cliente("José", "876.456.345-87", "Rua X Bairro Y", "86988995544", date.fromisoformat("2000-10-01"))
    conta1 = Conta(1, 50, cliente1)

    data_abertura2 = datetime.fromisoformat("2024-10-05T09:40:00")
    conta2 = Conta(2, 100, cliente1, data_abertura2)

    print(f"Titular da conta {conta1.numero} é {conta1.cliente.nome}")
    print(f"Titular da conta {conta2.numero} é {conta2.cliente.nome}")

teste_data_abertura()
teste_transferencia()
teste_conta_com_cliente()