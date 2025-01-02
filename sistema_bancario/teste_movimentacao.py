from movimentacao import Movimentacao

movimentacao1 = Movimentacao(nome="Saque", valor=100)
print(f"{movimentacao1.data} - {movimentacao1.nome} - R$ {movimentacao1.valor}")