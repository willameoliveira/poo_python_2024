from produto import Produto
import os
os.system("clear") #limpar a tela do terminal

produto1 = Produto(descricao="Mouse sem fio", valor=49.90, estoque=30)
produto2 = Produto("Camisa M", 50)

produto2.descricao = "Camisa Polo"
print(f"Estoque de {produto2.descricao}: {produto2.estoque}")

produto1.incrementar_estoque(20)
print(f"Estoque de {produto1.descricao}: {produto1.estoque}")

produto1.decrementar_estoque(20)
print(f"Estoque de {produto1.descricao}: {produto1.estoque}")

if not produto1.decrementar_estoque(31): #if produto1.decrementar_estoque(31) == False
    print("Estoque insuficiente.")

print(f"Estoque de {produto1.descricao}: {produto1.estoque}")

produto2.incrementar_estoque(10)
print(f"Estoque de {produto2.descricao}: {produto2.estoque}")

produto1.valor = 60
produto2.valor = -30
print(f"Valor do {produto1.descricao}: R$ {produto1.valor}")
print(f"Valor do {produto2.descricao}: R$ {produto2.valor}")