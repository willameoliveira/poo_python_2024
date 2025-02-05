from produto import Produto
from venda import Venda
import os

os.system("clear")
produto1 = Produto("Mouse sem fio", 50, 30)

venda1 = Venda(forma_pagamento="Cartão de crédito")
venda1.adicionar_item(produto=produto1, quantidade=2)

produto2 = Produto("Teclado", 15, 30)

venda1.adicionar_item(produto=produto2, quantidade=1)

print(venda1) #chamando o método __str__ implicitamente

print(f"Troco (valor pago 500): R$ {venda1.calcular_troco(500)}")