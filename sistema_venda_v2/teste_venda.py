from produto import Produto
from venda import Venda

produto1 = Produto(descricao="mouse",valor=100,estoque=2)
produto2 = Produto(descricao="pendrive",valor=50,estoque=7)
produto3 = Produto(descricao="monitor",valor=1000,estoque=10)
venda1 = Venda(forma_pagamento="Cartao")
venda1.adicionar_item(produto=produto1, quantidade=1)
venda1.adicionar_item(produto=produto2, quantidade=4)
venda1.adicionar_item(produto=produto3, quantidade=3)

print(venda1)
print(f"Troco R$ {venda1.calcular_troco(3500)}")