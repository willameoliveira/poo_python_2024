from conta import Conta
import os

os.system("clear")

conta = Conta(1, 100, "10/10/2024")
conta.depositar(500)
conta.ver_saldo()

if conta.sacar(500):
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente!")

conta.ver_saldo()