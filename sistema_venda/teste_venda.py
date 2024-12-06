from produto import Produto
from venda import Venda

produto1 = Produto("Mouse sem fio", 49.90, 30)

venda1 = Venda(produto=produto1, 
               quantidade_vendida=10, 
               forma_pagamento="Cartão de crédito")
print(venda1)
print(f"Troco (valor pago 500): R$ {venda1.calcular_troco(500)}")