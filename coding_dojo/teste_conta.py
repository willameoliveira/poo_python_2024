from conta import Conta
from movimentacao import Movimentacao
import os

os.system("clear") #limpar o terminal

conta2 = Conta(243, 190.12, "Flavio")       

conta1 = Conta(244, 150.12, "Felipe")       
conta1.depositar(140)
conta1.sacar(100)
conta1.transferir(conta2, 43)

print(f"extrato da conta {conta1.numero}: ")
for movimentacao in conta1.ver_extrato():
    print(movimentacao)

print(f"\n extrato da conta {conta2.numero}: ")
for movimentacao in conta2.ver_extrato():
    print(movimentacao)

print(f"\nTotal de contas: {Conta.get_total_contas()}")